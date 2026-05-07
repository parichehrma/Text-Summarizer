# Imports a tool to work with file paths in a clean way.
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml") # Creates a path object pointing to the config file.
PARAMS_FILE_PATH = Path("params.yaml") # Creates a path object pointing to the model parameters file.