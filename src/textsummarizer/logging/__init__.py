# This code sets up a system that prints logs on terminal + saves them into a file
# with timestamps and structure.

import os # Used to work with folders/files (create paths, directories)
import sys # Gives access to system features (like terminal output)
import logging # Python built-in tool to record logs (messages about what your code is doing)

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 
# This defines log format: asctime → time, levelname → INFO / ERROR / etc., module → file name
# message → actual log text

log_dir = "logs" # Folder name where logs will be stored

log_filepath = os.path.join(log_dir,"running_logs.log") # Full path of log file

os.makedirs(log_dir, exist_ok=True) # Creates the logs folder if it doesn’t exist, exist_ok=True → don’t crash if folder already exists



logging.basicConfig( # Configures how logging should work
    level= logging.INFO, # Only show logs of level INFO and above (so DEBUG is ignored)
    format= logging_str, # Applies your custom log format

    handlers=[ # Where logs should go
        logging.FileHandler(log_filepath), # Save logs into file (running_logs.log)
        logging.StreamHandler(sys.stdout) # Also print logs in terminal (console)
    ]
)

logger = logging.getLogger("textSummarizerLogger") # Creates a logger object (your personal logger)