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
    # TODO: Get the API key from environment variables
    # Hint: Use os.getenv() to get the API_KEY environment variable
    # If it's not set, print an error message and exit
    api_key = None  # Replace with your code

    if not api_key:
        print("Error: API key not found. Please add it to your .env file.")
        sys.exit(1)

    # TODO: Initialize the Gemini client with your API key
    # Hint: Use genai.Client() with the api_key field
    client = None  # Replace with your code

    # TODO: Define a system prompt for your agent
    # This determines your agent's personality and capabilities
    # Hint: Make it friendly, helpful, and give it a specific role
    SYSTEM_PROMPT = """
    # Replace with your system prompt
    """

    # TODO: Create a configuration for the Gemini client
    # Hint: Use GenerateContentConfig with your system prompt
    # For safety settings, we recommend using the default values
    config = None  # Replace with your code

    # Model name to use
    model_name = "gemini-2.0-flash"  # A good default model for chat

    # Initialize the conversation history
    contents = []

    print("\n🤖 Welcome to your Gemini Chat Agent! Type 'exit' to quit.")

    # TODO: Implement the chat loop
    # Hint: This should:
    # 1. Get user input
    # 2. Add it to conversation history using:
    #    contents.append(Content(role="user", parts=[Part(text=user_input)]))
    # 3. Send to Gemini and get a response
    # 4. Add the response to conversation history using Content and Part classes as above, with "model" role
    # 5. Print the response
    # 6. Loop until the user types "exit" or "quit"

    # Your chat loop code goes here


if __name__ == "__main__":
    main()
