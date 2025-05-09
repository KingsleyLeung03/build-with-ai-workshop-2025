# Module 4: Building an Autonomous Code Agent

This module demonstrates how to build an autonomous code agent that can interpret natural language instructions and perform file operations. The agent uses Gemini to understand user requests and execute appropriate actions through function calling.

## Files in this Module

1. `file_operations.py` - Contains utility functions for file system operations:
   - `list_files()` - Lists all files and directories in a specified path
   - `read_file()` - Reads and returns the contents of a file
   - `write_file()` - Writes content to a file

2. `code_agent.py` - The main agent implementation that:
   - Defines function declarations for Gemini
   - Creates a chat loop for user interaction
   - Handles function calls from the model
   - Routes function calls to the appropriate file operations

## How to Use

1. Configure Gemini API Key:
   ```bash
   # Create or edit your .env file
   echo "API_KEY=YOUR_GEMINI_API_KEY" > .env
   ```

2. Run the code agent:
   ```
   python extra-for-experts/code-agent/starter/code_agent.py
   ```

3. Interact with the agent by giving natural language instructions like:
   - "List all files in the current directory"
   - "Read the content of file_operations.py"
   - "Create a new Python file called hello.py that prints 'Hello World'"

## Learning Objectives

- Implement file system operations in Python
- Configure Gemini for function calling
- Create a conversational agent that can understand and execute tasks
- Handle the results of function calls and return them to the model

You can extend this agent by adding more functions or enhancing the existing ones to create a more powerful code assistant. 