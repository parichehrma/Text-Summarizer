import os # Used to work with files and folders
from pathlib import Path
import logging

# Logging format: 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')



# A list of file names and folders you want to automatically create in your project:

###  Create .github/workflows/.gitkeep: we use this folder code for deployment CI/CD
# Purpose: Sets up a folder for GitHub Actions (CI/CD deployment).
# Why .gitkeep: Git cannot commit empty folders, so we add this hidden file to keep the folder in Git.
# Use: Later, this folder will store workflow files that automatically deploy your code to the cloud whenever you
#  commit. when commite the code, automatically get code from this github folder and do deployment in your cloud

### Create src/{project_name}/__init__.py: Create SRC folder for sources (use f for string)
# Purpose: Marks your project folder as a Python package and local package then you can do import operation.
# Use: Allows you to import your code like a normal module. Makes folder a Python package for local imports
#  __init__.py: Create constructor file for install local package and do import operation.
# so Python treats the folder as a package, allowing you to import your code locally.

### src/{project_name}/components/__init__.py
# Purpose: A subpackage for components or modules of your project.
# Use: Organizes your code into logical parts.

### src/{project_name}/utils/__init__.py
# Purpose: A subpackage for utility/helper functions.
# Use: Keeps reusable code separate from main logic.

# .github/workflows/ → for CI/CD pipelines
# src/{project_name}/ → main code
# __init__.py → makes folder a package, this code creates local package.
# components/ → project components
# utils/ → helper functions


project_name = "textsummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", #Keeps an empty folder in Git (Git doesn’t track empty folders)
    f"src/{project_name}/__init__.py", #Makes this folder a Python package
    f"src/{project_name}/components/__init__.py", #for reusable parts (like data loader, model, etc.)
    f"src/{project_name}/utils/__init__.py", #Utility functions folder
    f"src/{project_name}/utils/common.py", #Common helper functions (used everywhere), avoid repeating code Put small reusable functions here
    f"src/{project_name}/logging/__init__.py", #For logging system (track errors, info),track what happens in your app Instead of print(), you use logging
    f"src/{project_name}/config/__init__.py", #This folder (config) should be treated like a package (module),config is a package, You can import files inside it
    f"src/{project_name}/config/configuration.py", #Reads settings (like file paths, parameters).central place to read settings.Instead of hardcoding paths. If path changes,update once here (very important in real jobs)
    f"src/{project_name}/pipeline/__init__.py",#ML pipeline steps (data → model → evaluation). organize ML steps. Real ML is a pipeline: data ingestion, preprocessing, training, evaluation. Keeps workflow structured (not messy in main.py)
    f"src/{project_name}/entity/__init__.py",#Data classes (define structure of data/config). define data structure (clean + typed). Makes code safer and easier to understand.
    f"src/{project_name}/constants/__init__.py",#Store fixed values (paths, names)
    "config/config.yaml", #Main configuration (paths, settings). external config file (VERY important).You can change behavior without touching code. Used in production systems
    "params.yaml", #Model parameters (learning rate, epochs, etc.)
    "app.py",#For web app (like Flask / Streamlit). build UI / API. Ex: Flask → API, Streamlit → dashboard . Lets users interact with your model
    "main.py",#Main script to run the project. entry point of project. Runs everything (pipeline, training, etc.)
    "Dockerfile",#To run project in Docker (same environment everywhere)
    "requirements.txt",#List of Python libraries to install
    "setup.py",#Makes project installable as a package
    "research/trials.ipynb",#Jupyter notebook for experiments

]


# Go through each file one by one:

for filepath in list_of_files:
    filepath = Path(filepath) # Fix path format, detect which os using and then return correct format path based on os
    filedir, filename = os.path.split(filepath) # split folder and file and put in filedir and filename
    
# Folder:
    # Need to check filedir not empty and then run, if it is empty means there is no folder:
    # Check if there is a folder path (some files like "app.py" don’t have a folder)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #Create the folder, exist_ok=True = don’t give error if folder already exists
        logging.info(f"Creating directory:{filedir} for the file {filename}") #Print/log a message, Helps you see what the program is doing
# File:
    # Always use filepath when: checking file existence, opening files, creating files.
    # if use filename, Python will check in the current working directory only but when use filepath, Python knows the exact location and checks the correct folder

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #If file doesnt exist OR empty → create it
        with open(filepath,'w') as f: # Open file in write mode. Creates file if it doesn’t exist. check size to see if not empty, i am not going to replace the file so ignore that file and create other file if empty replreplace it.
            pass # Do nothing (just create empty file)
            logging.info(f"Creating empty file: {filepath}") # Print/log message that file was created


    
    else:
        logging.info(f"{filename} already exists") # If file already exists AND not empty. Do nothing, just log message


