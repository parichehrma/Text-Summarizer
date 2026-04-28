import setuptools
from setuptools import setup, find_packages

# First Initialize ReadMe file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0" # First version

REPO_NAME = "Text-Summarizer"            # Repo Name
AUTHOR_USER_NAME = "parichehrma"         # Github Name
SRC_REPO = "textsummarizer"              # SRC Name
AUTHOR_EMAIL = "parichehr.ma@gmail.com"  # #mail Address



setuptools.setup(
    name=SRC_REPO, 
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown", # Tells this description is written in Markdown.
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, # Tells Python code is inside src folder.
    packages=setuptools.find_packages(where="src") # Automatically finds all Python packages inside src.
)