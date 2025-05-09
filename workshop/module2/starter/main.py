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

    # TODO: Update the system prompt to guide Gemini on when to use functions
    # The system prompt should:
    # 1. Introduce the assistant's role (weather-aware helper)
    # 2. Explain the available weather function and its capabilities
    # 3. Specify when to use the weather function (e.g., for location-specific weather queries)
    # 4. Include guidelines for formatting weather information in responses
    SYSTEM_PROMPT = """You are a helpful, friendly assistant with access to real-time weather information.

    # Add your system prompt here following the guidelines above
    """

    # TODO: Update the configuration to include the function declaration
    # 1. Create a Tool object with the get_weather_declaration
    # 2. Add it to the GenerateContentConfig
    config = GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        # Add the Tool configuration here:
        # tools=[Tool(function_declarations=[get_weather_declaration])]
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

            # TODO: Handle function calls
            # 1. Check if response.function_calls exists
            # 2. If it does, get the first function call
            # 3. Process the function call using process_function_call()
            # 4. Add both the function call and its result to the conversation history
            # 5. If no function calls, proceed with normal response handling

            if response.function_calls:
                # Add your function handling code here. For each function call:

                # Add the function call to the conversation history
                # Hint: use the `function_call` parameter of the `Part` class

                # Add the function result to the conversation history
                # Hint: use the `from_function_response` method of the `Part` class
                # e.g.
                # Part.from_function_response(name=..., response=...)

                # Add response to conversation history and print it
                pass

            # Add response to conversation history and print it
            contents.append(Content(role="model", parts=[Part(text=response.text)]))
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
    # TODO: Implement function call processing
    # 1. Get the function name from tool_call.name
    # 2. Get the arguments from tool_call.args
    # 3. Call the appropriate function (get_weather)
    # 4. Return the result

    # Example implementation:
    # if tool_call.name == "get_weather":
    #     return get_weather(**tool_call.args)
    # else:
    #     raise ValueError(f"Unknown function: {tool_call.name}")
    pass


if __name__ == "__main__":
    main()
