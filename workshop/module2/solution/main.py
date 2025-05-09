"""
Module 2: Adding Function Calling Capabilities

This script demonstrates how to create a chat agent with Google's Gemini API
that can call functions to retrieve information.
"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai.types import Content, Part, FunctionCall, GenerateContentConfig, Tool

# Import the function declarations and implementations
from tools import (
    get_weather_declaration,
    get_weather,
)

# Load environment variables
load_dotenv()


def main():
    # Get the API key from environment variables
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API key not found. Please add it to your .env file.")
        sys.exit(1)

    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)

    # Updated system prompt to guide Gemini on when to use functions
    SYSTEM_PROMPT = """You are a helpful, friendly assistant with access to real-time weather information.

    You have access to a get_weather function that can provide current weather data for various cities.
    When a user asks about weather, temperature, or conditions in a specific location, use the get_weather function.
    
    Important guidelines:
    - Only use the function when the user specifically asks about weather.
    - Extract the location from the user's query to pass to the function.
    - Don't make up weather information - use the function to get accurate data.
    - When responding about weather, include details like temperature, conditions, humidity, etc.
    """

    # Configuration with function declaration
    config = GenerateContentConfig(
        tools=[Tool(function_declarations=[get_weather_declaration])],
        system_instruction=SYSTEM_PROMPT,
    )

    # Model name to use
    model_name = "gemini-2.0-flash"

    # Initialize the conversation history
    contents = []

    print("\n🤖 Welcome to your Gemini Function Calling Agent! Type 'exit' to quit.")

    # Chat loop
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()

            # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("\n👋 Goodbye!")
                break

            # Skip empty inputs
            if not user_input:
                continue

            # Add user message to conversation history
            contents.append(Content(role="user", parts=[Part(text=user_input)]))

            # Get response from Gemini
            response = client.models.generate_content(
                model=model_name, contents=contents, config=config
            )

            # Check if Gemini wants to call a function
            if response.function_calls:
                try:
                    # Loop through all function calls
                    for function_call in response.function_calls:
                        print(f"\n🔧 Executing function: {function_call.name}")
                        # Process the function call
                        result = process_function_call(function_call)

                        # Add function call to conversation history
                        contents.append(
                            Content(
                                role="model", parts=[Part(function_call=function_call)]
                            )
                        )

                        # Add function result to conversation history
                        contents.append(
                            Content(
                                role="user",
                                parts=[
                                    Part.from_function_response(
                                        name=function_call.name,
                                        response={"result": result},
                                    )
                                ],
                            )
                        )

                    # Get Gemini's final response after processing the function result
                    final_response = client.models.generate_content(
                        model=model_name, contents=contents, config=config
                    )

                    # Add response to conversation history
                    contents.append(
                        Content(role="model", parts=[Part(text=final_response.text)])
                    )

                    # Print the response
                    print(f"\n🤖 Gemini: {final_response.text.strip()}")

                except Exception as e:
                    print(f"\n❌ Error executing function: {str(e)}")
                    # Add error message to conversation
                    contents.append(
                        Content(
                            role="user",
                            parts=[
                                Part.from_function_response(
                                    name=function_call.name, response={"error": str(e)}
                                )
                            ],
                        )
                    )
            else:
                # No function calls, add response to conversation history
                contents.append(Content(role="model", parts=[Part(text=response.text)]))

                # Print the response
                print(f"\n🤖 Gemini: {response.text.strip()}")

        
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


def process_function_call(tool_call: FunctionCall) -> dict:
    """
    Process a function call from Gemini and return the result.

    Args:
        tool_call: The function call object from Gemini

    Returns:
        dict: The result of the function call
    """
    # Get function name and arguments
    function_name = tool_call.name
    args = tool_call.args

    # Call the appropriate function
    if function_name == "get_weather":
        return get_weather(**args)
    else:
        raise ValueError(f"Unknown function: {function_name}")


if __name__ == "__main__":
    main()
