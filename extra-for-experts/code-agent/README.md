# Building an Autonomous Code Agent

In this module, you'll learn how to create an autonomous code agent that can interact with the file system based on natural language instructions. This agent will be able to list directories, read files, and write code to create new files or modify existing ones.

## Concepts

### 1. File System Operations

Instead of weather information, your agent will now work with the file system using these functions:

- `list_files`: Shows contents of a directory
- `read_file`: Gets the content of a file
- `write_file`: Creates or modifies a file with specified content

### 2. Autonomous Reasoning

For a code agent to work effectively, the system prompt needs to instruct Gemini on how to:

1. Break down complex requests into steps
2. Determine which files to read or examine first
3. Plan what code to generate
4. Decide where to create or modify files

### 3. Context Management

The code agent needs to keep track of:

- Which files it has seen
- What code it has already written
- The user's requirements and any clarifications

### 4. Complex Function Chaining

Code generation often requires multiple sequential operations:

```
User: "Create a simple Flask web app with a homepage"

list_files(directory=".") -> See what already exists
write_file(path="app.py", content="Flask code...") -> Create app file
write_file(path="templates/index.html", content="HTML...") -> Create template
```

## Exercise: Build a Code Agent

Your task is to:

1. Implement the file operation functions (`list_files`, `read_file`, `write_file`)
2. Create function declarations for these operations
3. Update the system prompt to guide Gemini on how to act as a code agent
4. Set up the function chaining loop to allow multi-step operations
5. Test your agent with programming tasks

## Getting Started

1. Navigate to the `starter` directory
2. Open `main.py` and `tools.py`
3. Follow the TODO comments to complete the exercise

## Testing Your Solution

Run your agent and try these requests:

- "List the files in the current directory"
- "Create a simple Python script that prints Hello World"
- "Create a basic calculator in HTML, CSS, and JavaScript"
- "Check if there's a README file and if not, create one"

## Solution

Once you've completed the exercise, you can check the `solution` directory to compare your implementation.
