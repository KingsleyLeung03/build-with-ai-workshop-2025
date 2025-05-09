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

    # System prompt with instructions for function chaining
    SYSTEM_PROMPT = """You are a helpful, friendly assistant with access to real-time weather information.

    You have access to these functions:
    - get_current_location: Gets the user's current city and country
    - get_weather: Gets the current weather for a location
    - convert_temperature: Converts temperatures between Celsius and Fahrenheit

    When chaining functions:
    1. If a user asks about weather in "my location" or "here", first call get_current_location, then use that city in get_weather
    2. If a user asks for temperature in a different unit, first get the weather, then convert the temperature
    3. For comparisons between locations, get weather for both locations before responding

    Important guidelines:
    - Always use get_current_location when the user refers to their current location
    - Always use convert_temperature when the user wants temperatures in a specific unit
    - Don't make up weather information - use the functions to get accurate data
    - Chain functions together when needed to fully answer the user's query
    """

    # Configuration with all function declarations
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

            # Function chaining loop - keep calling functions until we get a final response
            function_calling_in_process = True
            while function_calling_in_process:
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

                        # Continue the loop to check for more function calls
                        continue

                    except Exception as e:
                        print(f"\n❌ Error executing function: {str(e)}")
                        # Add error message to conversation
                        contents.append(
                            Content(
                                role="user",
                                parts=[
                                    Part.from_function_response(
                                        name=function_call.name,
                                        response={"error": str(e)},
                                    )
                                ],
                            )
                        )
                        function_calling_in_process = False
                else: # If there are no more function calls, add the response to the conversation history
                    contents.append(
                        Content(role="model", parts=[Part(text=response.text)])
                    )

                    # Print the final response
                    print(f"\n🤖 Gemini: {response.text.strip()}")
                    function_calling_in_process = False

        
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
    elif function_name == "get_current_location":
        return get_current_location()
    elif function_name == "convert_temperature":
        return convert_temperature(**args)
    else:
        raise ValueError(f"Unknown function: {function_name}")


if __name__ == "__main__":
    main()
