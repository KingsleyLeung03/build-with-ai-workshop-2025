# GDGC Build with AI Workshop

Welcome to the GDGC Build with AI Workshop! This hands-on workshop will teach you how to use Google's Gemini API to create AI agents that can call custom functions based on natural language input.

## Prerequisites

- Python 3.11 or higher
- A Google Cloud account with access to Vertex AI
- Basic understanding of Python and async programming
- Your Google Cloud API key

## Setup Instructions

1.  **Setup the codebase**

    _Using Firebase Studio:_

    1.  Go to [Firebase Studio](https://studio.firebase.google.com/)
    2.  Click "Import Repo"
    3.  Enter the work repository URL:

    `https://github.com/Developer-Student-Club-UoA/build-with-ai-workshop-2025`

    4.  Wait for the codebase to initialise and setup to complete. You will know once the README opens. While you wait for this, you can go to **step 2** of the setup instructions _(Get Gemini API key)_.

    _Setting up the project locally:_ \
     _(if you setup with firebase, skip to step 2)_

    1.  **Fork the Repository**

    2.  **Clone your forked repository**

        ```bash
        git clone https://github.com/Developer-Student-Club-UoA/build-with-ai-workshop-2025.git
        cd build-with-ai-workshop-2025
        ```

    3.  **Set Up Your Python Environment**

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

    4.  **Get Gemini API key**

        > _Note: university accounts do not support Google AI studio, we recommend signing up with your personal email._

        Head to the [AI studio website](https://aistudio.google.com/apikey) to get setup.

## Project Structure

```
.
├── README.md
└── workshop/
    ├── module1        # Basic setup and configuration of Gemini agent
    ├── module2        # Single function calling implementation
    └── module3        # Advanced function chaining and conversation flow
        ├── main.py        # Main application with Gemini agent
        └── tools.py       # Function declarations and implementations
```

## Understanding the Code

### 1. Function Declarations (`tools.py`)

The `tools.py` file contains two key components for each function:

- A **function declaration** that tells Gemini what the function does and what parameters it expects
- The actual **function implementation** that executes when Gemini calls it

Example:

```python
get_current_weather_declaration = {
    "name": "get_current_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name (e.g. 'San Francisco', 'New York', 'London')"
            }
        },
        "required": ["location"]
    }
}

def get_current_weather(location: str) -> dict:
    """
    Corresponds to the get_current_weather_declaration.
    Will fetch the weather given a location.
    """
```

### 2. Gemini Agent (`main.py`)

The `main.py` file contains the `GeminiAgent` class that:

- Initializes the Gemini client with system instructions
- Manages the conversation and function context
- Processes responses and chats

## Workshop Modules

### Module 1: Setting up the Gemini Agent

1. Set up your environment variables and authentication
2. Initialize the Gemini client with basic chat capabilities
3. Test basic conversations with the agent

### Module 2: Adding New Functions

1. Create new function declarations
2. Implement the functions with context awareness
3. Add them to the agent's available tools

### Module 3: Chaining functions

1. Learn how to chain multiple functions together to solve complex queries
2. Handle function dependencies and order of operations
3. Practice with example scenarios like:
   - Getting weather for current location (chains location + weather)
   - Converting temperatures between units (chains weather + conversion)
   - Comparing weather in different cities (chains multiple weather calls)

## Running the Application

1. Configure Gemini API Key:

   ```bash
   # Create or edit your .env file
   echo "API_KEY=YOUR_GEMINI_API_KEY" > .env
   ```

2. Run the application:

   ```bash
   python src/main.py
   ```

3. Try some example queries:
   - "What's the current weather in the captial of Japan?"
   - "How hot is it in my location?"

### Getting Help

- [Gemini API documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini)
- [Project IDX documentation](https://idx.dev/docs)
- [Firebase documentation](https://firebase.google.com/docs)
- [Google Cloud Authentication guide](https://cloud.google.com/docs/authentication)

## Next Steps

After completing the workshop:

1. Explore advanced Gemini features
2. Add more complex function capabilities
3. Add more complex function chains
4. Implement persistent conversation storage

## License

This workshop material is licensed under the MIT License. See the LICENSE file for details.
