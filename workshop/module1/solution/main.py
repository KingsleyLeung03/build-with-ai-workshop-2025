"""
Module 1: Setting Up Your First Gemini Chat Agent

This script creates a basic chat agent using Google's Gemini API.
"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai.types import Content, Part, GenerateContentConfig

# Load environment variables
load_dotenv()


def main():
    # Get the API key from environment variables
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API key not found. Please add it to your .env file.")
        sys.exit(1)

    # Initialize the Gemini client with your API key
    client = genai.Client(api_key=api_key)

    # Define a system prompt for your agent
    SYSTEM_PROMPT = """You are a helpful, friendly, and knowledgeable assistant.
    You provide accurate information and are good at having natural conversations.
    If you don't know something, you'll admit it rather than making up an answer.
    Try to be concise but informative in your responses.
    """

    # Create a configuration for the Gemini client
    config = GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
    )

    # Model name to use
    model_name = "gemini-2.0-flash"

    # Initialize the conversation history
    contents = []

    print("\n🤖 Welcome to your Gemini Chat Agent! Type 'exit' to quit.")

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

            # Add response to conversation history
            contents.append(Content(role="model", parts=[Part(text=response.text)]))

            # Print the response
            print(f"\n🤖 Gemini: {response.text.strip()}")

        
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
