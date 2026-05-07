import os # Used to interact with the operating system (files, folders, paths).
from box.exceptions import BoxValueError # An error raised when there is a problem with values in a ConfigBox.
import yaml # Used to read and write YAML files (configuration files).
from textsummarizer.logging import logger # Custom logging tool to track events, errors, and messages in the project.
from ensure import ensure_annotations # Ensures function input types match the expected types (type validation).
from box import ConfigBox # Allows dictionary items to be accessed using dot notation (e.g., data.key instead of data["key"]).
from pathlib import Path # Used for handling file and directory paths in a clean and modern way.
from typing import Any # Represents a variable that can be of any data type.



# Function to read a YAML file and return its full content.
@ensure_annotations # Makes sure function inputs have correct data types.
# Defines a function that takes a file path and returns a ConfigBox.

def read_yaml(path_to_yaml: Path) -> ConfigBox: 
    # Simple description of the function.
    """reads yaml file and returns 

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file: # Opens the YAML file.
            content = yaml.safe_load(yaml_file) # Reads and converts YAML file into Python dictionary.
            logger.info(f"yaml file: {path_to_yaml} loaded successfully") # Prints success message in logs.
            return ConfigBox(content) # Converts dictionary to ConfigBox (dot access) and returns it.
    except BoxValueError: # Handles error if YAML file is empty or invalid Box format.
        raise ValueError("yaml file is empty") # Shows error message if file has no content.
    except Exception as e: # Catches any other unexpected error.
        raise e # Re-throws the same error.
    

# Creates multiple folders (directories) and logs each one if verbose=True.
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True): # Defines a function to create multiple directories.
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories 
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    # Input: a list of folder paths.
    for path in path_to_directories: # Loops through each path in the list.
        os.makedirs(path, exist_ok=True) # Creates the directory (no error if it already exists).
        if verbose: # Checks if logging is enabled.
            logger.info(f"created directory at: {path}") # Logs a message showing the created directory.


# This function returns the file size in KB.
@ensure_annotations
def get_size(path: Path) -> str:# Function that takes a file path and returns its size as a string.
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024) # Gets file size in bytes, converts to KB, and rounds it.
    return f"~ {size_in_kb} KB" # Returns the size as a formatted string (e.g., "~ 25 KB").

    