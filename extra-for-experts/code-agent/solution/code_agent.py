"""
Module 4: Building an Autonomous Code Agent

This script implements an autonomous code agent that can interact with the file system
based on natural language instructions, using Google's Gemini API with function calling.
"""

import os
import sys
from google import genai
from google.genai.types import Content, Part, FunctionCall, GenerateContentConfig, Tool
from typing import List, Any
from dotenv import load_dotenv

# Import our file operation functions and declarations
from file_operations import (
    list_files,
    read_file,
    write_file,
    list_files_declaration,
    read_file_declaration,
    write_file_declaration,
)

# Load environment variables
load_dotenv()


class CodeAgent:
    """
    An autonomous code agent powered by Google's Gemini API with function calling capabilities.

    This agent can:
    1. List files in directories
    2. Read file contents
    3. Write or create files with specified content
    4. Chain these operations together to accomplish complex tasks
    """

    # System prompt to guide the model's behavior
    SYSTEM_PROMPT = """You are a helpful code assistant that can help users with file operations and coding tasks.
    
    You have access to the following functions:
    - list_files: Lists files in a directory
    - read_file: Reads the content of a file
    - write_file: Creates or modifies a file with specified content
    
    When helping users with coding tasks:
    1. Use list_files to understand what's in the current directory
    2. Use read_file to examine existing files if needed
    3. Use write_file to create new files or modify existing ones
    4. Chain these functions together to complete complex tasks
    
    Important guidelines:
    - Break down complex requests into logical steps
    - Always check if a file exists before trying to modify it
    - When creating new code files, include all necessary imports and make the code complete
    - When creating HTML/CSS/JS files, make sure they work together if they're part of a larger project
    - Provide clear explanations of what you're doing and why
    - Don't make assumptions about the content of files without reading them first
    
    Example workflow:
    1. User asks to create a Flask app - first list files to see what exists
    2. Create app.py with the Flask code
    3. Create templates directory and add HTML templates
    4. Explain how to run the application
    """

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash"):
        """
        Initialize the Code Agent.

        Args:
            api_key (str): Google Cloud API key
            model_name (str): Gemini model to use
        """
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

        # Initialize the configuration with our function declarations
        self.config = GenerateContentConfig(
            tools=[
                Tool(
                    function_declarations=[
                        list_files_declaration,
                        read_file_declaration,
                        write_file_declaration,
                    ]
                )
            ],
            system_instruction=self.SYSTEM_PROMPT,
            temperature=0.2,  # Lower temperature for more precise coding
        )

    def process_function_call(self, tool_call: FunctionCall) -> Any:
        """
        Process a function call from Gemini and return the result.

        Args:
            tool_call: The function call object from Gemini

        Returns:
            The result of the function call

        Raises:
            ValueError: If the function name is unknown
        """
        function_name = tool_call.name
        args = tool_call.args

        try:
            match function_name:
                case "list_files":
                    directory = args.get("directory", ".")
                    return list_files(directory)
                case "read_file":
                    file_path = args.get("file_path")
                    return read_file(file_path)
                case "write_file":
                    file_path = args.get("file_path")
                    content = args.get("content")
                    return write_file(file_path, content)
                case _:
                    raise ValueError(f"Unknown function: {function_name}")
        except Exception as e:
            return f"Calling {function_name} failed: {str(e)}"

    def run(self):
        """Run the interactive code agent session."""
        print("\n🤖 Welcome to the Code Agent! Type 'exit' to quit.")
        print("Ask me to create files, write code, or explore the directory structure.")
        print("For example: 'Create a simple Flask web app with a home page'")
        print("-" * 80)

        # Initialize conversation history
        contents: List[Content] = []

        while True:
            try:
                # Get user input
                user_input = input("\n👤 You: ").strip()

                # Check for exit command
                if user_input.lower() in ["exit", "quit"]:
                    print("\n👋 Goodbye!")
                    break
                if not user_input:
                    continue

                # Add user message to conversation
                contents.append(Content(role="user", parts=[Part(text=user_input)]))

                # Function calling loop - continue until no more function calls
                while True:
                    # Get Gemini's response
                    response = self.client.models.generate_content(
                        model=self.model_name, contents=contents, config=self.config
                    )

                    # Check if Gemini wants to call a function
                    if response.function_calls:
                        tool_call = response.function_calls[0]
                        print(
                            f"\n🔧 Executing function: {tool_call.name} with args: {tool_call.args}"
                        )

                        try:
                            # Process the function call
                            result = self.process_function_call(tool_call)

                            # Add function call to conversation history
                            contents.append(
                                Content(
                                    role="model", parts=[Part(function_call=tool_call)]
                                )
                            )

                            # Add function result to conversation history
                            contents.append(
                                Content(
                                    role="user",
                                    parts=[
                                        Part.from_function_response(
                                            name=tool_call.name,
                                            response={"result": result},
                                        )
                                    ],
                                )
                            )

                            # Continue the loop to check for more function calls
                            continue

                        except Exception as e:
                            print(f"\n❌ Error executing function: {str(e)}")
                            break

                    # No more function calls, add response to conversation history
                    contents.append(
                        Content(role="model", parts=[Part(text=response.text)])
                    )

                    # Print the final response
                    print(f"\n\033[92mAgent\033[0m: {response.text.strip()}")
                    break  # Exit the function calling loop

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")


def main():
    """Main entry point for the code agent."""
    # Get the Google Cloud API key from environment variables
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API key not found. Please add it to your .env file.")
        sys.exit(1)

    # Create and run the code agent
    agent = CodeAgent(api_key=api_key)
    agent.run()


if __name__ == "__main__":
    main()
