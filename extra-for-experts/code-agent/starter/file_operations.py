import os
import json
from typing import List, Optional

# TODO: Define function declarations for Gemini to understand our file operations
# Each declaration should include:
# - name: The name of the function
# - description: What the function does
# - parameters: What parameters the function takes, their types, and descriptions
# - required: Which parameters are required

# Example declaration format:
# function_declaration = {
#     "name": "function_name",
#     "description": "Description of what the function does",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "param_name": {
#                 "type": "string",
#                 "description": "Description of the parameter"
#             }
#         },
#         "required": ["param_name"]
#     }
# }

# Declaration for list_files
list_files_declaration = {
    # TODO: Complete this declaration
}

# Declaration for read_file
read_file_declaration = {
    # TODO: Complete this declaration
}

# Declaration for write_file
write_file_declaration = {
    # TODO: Complete this declaration
}


def list_files(directory: str = ".") -> List[str]:
    """
    List all files and directories in the specified path.

    Args:
        directory: The directory path to list files from (default: current directory)

    Returns:
        A list of filenames and directories
    """
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []


def read_file(file_path: str) -> Optional[str]:
    """
    Read and return the contents of a file.

    Args:
        file_path: Path to the file to read

    Returns:
        The contents of the file as a string, or None if there was an error
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def write_file(file_path: str, content: str) -> bool:
    """
    Write content to a file.

    Args:
        file_path: Path to the file to write
        content: Content to write to the file

    Returns:
        True if successful, False otherwise
    """
    try:
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False
