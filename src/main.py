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
    # Hint: Use os.getenv() to get the API_KEY environment variable
    # If it's not set, print an error message and exit
    api_key = os.getenv("API_KEY")  # Replace with your code
    
    if not api_key:
        print("Error: API key not found. Please add it to your .env file.")
        sys.exit(1)
    
    # Initialize the Gemini client with your API key
    # Hint: Use genai.Client() with the api_key field
    client = genai.Client(api_key=api_key)  # Replace with your code
    
    # Define a system prompt for your agent
    # This determines your agent's personality and capabilities
    # Hint: Make it friendly, helpful, and give it a specific role
    SYSTEM_PROMPT = """
    You are a helpful assistant that provides information and answers questions.
    You can assist with a variety of topics, including technology, science, and general knowledge.
    Your goal is to provide accurate and concise information to the user.
    You should be friendly and approachable, making the user feel comfortable asking questions.
    You can also provide examples and explanations to help clarify complex topics.
    If you don't know the answer to a question, it's okay to say so.
    You should always strive to be helpful and informative.
    You are not a human, but you can simulate a conversation as if you were one.
    You are not allowed to provide any personal opinions or beliefs.
    """
    
    # Create a configuration for the Gemini client
    # Hint: Use GenerateContentConfig with your system prompt
    # For safety settings, we recommend using the default values
    config = GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
    ) 
    
    # Model name to use
    model_name = "gemini-2.0-flash"  # A good default model for chat
    
    # Initialize the conversation history
    contents = []
    
    print("\n🤖 Welcome to your Gemini Chat Agent! Type 'exit' to quit.")
    
    # Implement the chat loop
    # Hint: This should:
    # 1. Get user input
    # 2. Add it to conversation history
    # 3. Send to Gemini and get a response
    # 4. Add the response to conversation history
    # 5. Print the response
    # 6. Loop until the user types "exit" or "quit"
    
    # Your chat loop code goes here

    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() in ["exit", "quit"]:
                print("\n👋 Goodbye!")
                break
            
            if not user_input:
                print("Please enter a valid message.")
                continue

            # Add user input to conversation history
            contents.append(Content(role="user", parts=[Part(text=user_input)]))
            
            # Send the request to Gemini and get a response
            response = client.models.generate_content(
                model=model_name, contents=contents, config=config
            )
            
            # Add the response to conversation history
            contents.append(Content(role="model", parts=[Part(text=response.text)]))
            
            # Print the response
            print(f"\n🤖 Gemini: {response.text.strip()}")

            # Clear the conversation history if it gets too long
            if len(contents) > 10:
                contents = contents[-10:]
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main() 