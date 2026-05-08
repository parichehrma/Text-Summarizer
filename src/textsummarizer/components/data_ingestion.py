import os
import requests

import urllib.request as request 
import zipfile 
from textsummarizer.logging import logger 
from textsummarizer.utils.common import get_size 
from pathlib import Path
from textsummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config):
        self.config = config

    # -------------------------
    # DOWNLOAD
    # -------------------------
    def download_file(self):
        url = self.config.source_url
        file_path = self.config.local_data_file

        print(f"📥 Downloading: {url}")

        response = requests.get(url, stream=True)

        if response.status_code != 200:
            raise Exception(f"❌ Download failed: {response.status_code}")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"📦 Size: {os.path.getsize(file_path)} bytes")

    # -------------------------
    # SAFE EXTRACT (FIX FOR EOFError)
    # -------------------------
    def extract_zip_file(self):
        file_path = self.config.local_data_file
        unzip_path = self.config.unzip_dir

        print("📂 Extracting safely...")

        os.makedirs(unzip_path, exist_ok=True)

        try:
            with zipfile.ZipFile(file_path, "r") as zip_ref:

                # 🔥 Instead of extractall → extract file-by-file safely
                for member in zip_ref.infolist():
                    try:
                        zip_ref.extract(member, unzip_path)
                    except Exception as e:
                        print(f"⚠️ Skipping corrupted file: {member.filename} -> {e}")

            print(f"✅ Extraction completed at: {unzip_path}")

        except zipfile.BadZipFile:
            raise Exception("❌ Completely invalid ZIP file")

        except EOFError:
            raise Exception("❌ ZIP file is corrupted (EOFError during extraction)")