"""
Module 4: Building an Autonomous Code Agent

This script implements an autonomous code agent that can interact with the file system
based on natural language instructions, using Google's Gemini API with function calling.
"""

import os
import sys
from google import genai
from google.genai.types import Content, Part, FunctionCall, GenerateContentConfig, Tool
from typing import List, Dict, Any

# Import our file operation functions and declarations
from file_operations import (
    list_files,
    read_file,
    write_file,
    list_files_declaration,
    read_file_declaration,
    write_file_declaration,
)


class CodeAgent:
    """
    An autonomous code agent powered by Google's Gemini API with function calling capabilities.

    This agent can:
    1. List files in directories
    2. Read file contents
    3. Write or create files with specified content
    4. Chain these operations together to accomplish complex tasks
    """

    # TODO: Create a detailed system prompt to guide the model's behavior
    # The prompt should instruct Gemini on when and how to use the file operation functions
    # Include guidelines for creating code, checking files, and explaining what it's doing
    SYSTEM_PROMPT = """
    # Replace with your system prompt
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

        # TODO: Initialize the configuration with our function declarations
        # The configuration should include:
        # - tools: A list of Tool objects containing our function declarations
        # - system_instruction: The system prompt that guides Gemini's behavior
        # - temperature: A value controlling randomness (lower for more precise coding)
        self.config = None  # Replace with your code

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
        # TODO: Implement the function call handler
        # 1. Extract the function name and arguments
        # 2. Call the appropriate function based on the name
        # 3. Return the result
        pass

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

                # TODO: Implement the function calling loop
                # This loop should:
                # 1. Get a response from Gemini
                # 2. Check if Gemini wants to call a function
                # 3. If yes, process the function call and add the result to the conversation
                # 4. Continue this loop until Gemini doesn't call any more functions
                # 5. Then display the final response

                # Your function calling loop code goes here

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
