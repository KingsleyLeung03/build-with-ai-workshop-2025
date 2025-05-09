"""
Module 3: Chaining Functions Together

This script demonstrates how to chain multiple function calls together
using Google's Gemini API to solve complex queries.
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
    get_current_location_declaration,
    get_current_location,
    convert_temperature_declaration,
    convert_temperature,
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

    # TODO: Update the system prompt to guide Gemini on function chaining
    # The system prompt should:
    # 1. Introduce the assistant's role (weather-aware helper)
    # 2. List all available functions and their purposes
    # 3. Explain when to chain specific functions together:
    #    - get_current_location -> get_weather for "weather here"
    #    - get_weather -> convert_temperature for unit conversions
    # 4. Include guidelines for formatting responses
    SYSTEM_PROMPT = """You are a helpful, friendly assistant with access to real-time weather information.

    # Add instructions about function chaining here
    """

    # TODO: Update the configuration to include all function declarations
    config = GenerateContentConfig(
        tools=[
            Tool(
                function_declarations=[
                    get_weather_declaration,
                    get_current_location_declaration,
                    convert_temperature_declaration,
                ]
            )
        ],
        system_instruction=SYSTEM_PROMPT,
    )

    # Model name to use
    model_name = "gemini-2.0-flash"

    # Initialize the conversation history
    contents = []

    print("\n🤖 Welcome to your Gemini Function Chaining Agent! Type 'exit' to quit.")

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

            # TODO: Implement a function chaining loop
            # Hint: This should repeatedly:
            # 1. Get a response from Gemini
            # 2. Check if it wants to call a function
            # 3. If yes, process the function call and add the result to the conversation
            # 4. Continue this loop until Gemini doesn't call any more functions
            # 5. Then display the final response

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
    # TODO: Update to handle all functions
    # Add cases for other functions
    else:
        raise ValueError(f"Unknown function: {function_name}")


if __name__ == "__main__":
    main()
