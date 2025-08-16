import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "sub_project_1"

list_of_files = [
    "data/.gitkeep",
    "artifacts/results/.gitkeep",
    "artifacts/output/.gitkeep",
    "notebooks/trials.ipynb",

    f"src/{project_name}/data_pipeline/__init__.py",
    f"src/{project_name}/data_pipeline/stage_01.py",

    f"src/{project_name}/training_pipeline/__init__.py",
    f"src/{project_name}/training_pipeline/stage_01.py",

    f"src/{project_name}/evaluation_pipeline/__init__.py",
    f"src/{project_name}/evaluation_pipeline/stage_01.py",

    "utils/__init__.py",
    "utils/config.py",
    "utils/logger.py",
    "utils/helper.py",

    "main.py",
    "app.py",

    "tests/__init__.py",

    "params.yaml",
    "DVC.yaml",
    ".env.local",
    ".env.example",
]


for filepath in list_of_files:
    filepath = Path(filepath) #to solve the windows path issue
    filedir, filename = os.path.split(filepath) # to handle the project_name folder


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")