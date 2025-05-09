# Gemini Function Calling Workshop

A 2-hour workshop for beginners to learn how to use Google's Gemini API with function calling capabilities.

## Prerequisites

- Python 3.11 or higher
- A Gemini API Key
- Basic understanding of Python

## Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/build-with-ai-workshop-2025
.git
   cd build-with-ai-workshop-2025

   ```

2. Set up your Python environment:

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

   # Install dependencies
   pip install -e .
   ```

3. Configure Gemini API Key:
   ```bash
   # Create or edit your .env file
   echo "API_KEY=YOUR_GEMINI_API_KEY" > .env
   ```

## Workshop Modules

### Module 1: Setting Up Your First Gemini Chat Agent

Learn how to set up a basic chat agent with Gemini that can hold a conversation.

- Introduction to the Gemini API
- Creating a basic chat loop
- Managing conversation history
- Crafting effective system prompts

### Module 2: Adding Function Calling Capabilities

Add your first function to the Gemini agent and learn how to make the AI call it appropriately.

- Creating function declarations
- Implementing a weather information function
- Guiding Gemini on when to use functions
- Handling function results in conversation

### Module 3: Chaining Functions Together

Make your agent smarter by chaining multiple functions together to solve complex queries.

- Setting up dependent functions
- Managing function context and results
- Having Gemini call multiple functions in sequence
- Creating a more intelligent, interactive experience

## Workshop Standards

### Temperature and Units

- All weather data uses Celsius temperatures consistently across modules
- Weather data includes a "unit": "celsius" field for clarity
- Module 3 introduces temperature conversion between Celsius and Fahrenheit

### Module Progression

1. **Module 1**: Basic chat functionality

   - Simple system prompt
   - Basic error handling
   - No function calling

2. **Module 2**: Single function calling

   - Weather function with Celsius temperatures
   - Enhanced system prompt for weather queries
   - Basic function call handling
   - Improved error handling with conversation context

3. **Module 3**: Multiple function chaining
   - Additional location and temperature conversion functions
   - Complex system prompt for multi-function scenarios
   - Advanced error handling
   - Function call chaining logic

## Workshop Flow

Each module contains:

- `README.md`: Instructions and concepts
- `/starter`: Starting code for the exercise
- `/solution`: Completed solution for reference

Proceed through each module in order. Each builds on skills from the previous module.

## Resources

- [Gemini API documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini)
- [Google Cloud Authentication guide](https://cloud.google.com/docs/authentication)
- [Python Google AI SDK](https://github.com/google/generative-ai-python)
