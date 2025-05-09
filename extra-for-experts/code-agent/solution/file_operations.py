"""
This module contains function declarations and implementations for file system operations.
Each function has both an implementation and a corresponding declaration that tells Gemini how to use it.
"""

import os
from typing import List, Optional

# Function declaration for listing files
list_files_declaration = {
    "name": "list_files",
    "description": "List all files and directories in the specified path",
    "parameters": {
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": "The directory path to list files from (default: current directory)",
            }
        },
        "required": [],
    },
}

# Function declaration for reading files
read_file_declaration = {
    "name": "read_file",
    "description": "Read and return the contents of a file",
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {"type": "string", "description": "Path to the file to read"}
        },
        "required": ["file_path"],
    },
}

# Function declaration for writing files
write_file_declaration = {
    "name": "write_file",
    "description": "Write content to a file, creating directories if they don't exist",
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {"type": "string", "description": "Path to the file to write"},
            "content": {
                "type": "string",
                "description": "Content to write to the file",
            },
        },
        "required": ["file_path", "content"],
    },
}


def list_files(directory: str = ".") -> List[str]:
    """
    List all files and directories in the specified path.

    Args:
        directory (str): The directory path to list files from (default: current directory)

    Returns:
        List[str]: A list of filenames and directories

    Raises:
        OSError: If the directory doesn't exist or cannot be accessed
    """
    files = os.listdir(directory)
    return files


def read_file(file_path: str) -> Optional[str]:
    """
    Read and return the contents of a file.

    Args:
        file_path (str): Path to the file to read

    Returns:
        Optional[str]: The contents of the file as a string, or None if there was an error

    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If the file cannot be read
    """
    with open(file_path, "r") as file:
        return file.read()


def write_file(file_path: str, content: str) -> bool:
    """
    Write content to a file, creating directories if they don't exist.

    Args:
        file_path (str): Path to the file to write
        content (str): Content to write to the file

    Returns:
        bool: True if successful, False otherwise

    Raises:
        IOError: If the file cannot be written to
    """
    # Create directories if they don't exist
    dir_path = os.path.dirname(file_path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "w") as file:
        file.write(content)
    return True
