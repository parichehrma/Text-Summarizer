import os
import requests

import urllib.request as request 
import zipfile 
from textsummarizer.logging import logger 
from textsummarizer.utils.common import get_size 
from pathlib import Path
from textsummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self): 
        url = self.config.source_url 

        r = requests.get(url) 
        print("Status Code:", r.status_code) 
        print("Content Type:", r.headers.get("Content-Type")) 

        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True) 

        with open(self.config.local_data_file, "wb") as f: 
            f.write(r.content)


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir 
        os.makedirs(unzip_path, exist_ok=True)  
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref: 
            zip_ref.extractall(unzip_path) 
