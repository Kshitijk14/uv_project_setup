import os
import traceback
import sys
from utils import CONFIG, setup_logger


# setup logging
LOG_PATH = CONFIG["LOG_PATH"]
LOG_DIR = os.path.join(os.getcwd(), LOG_PATH)
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "main.log")


def main():
    logger = setup_logger("main_logger", LOG_FILE)

    logger.info("Hello from uv-project-setup!")
    try:
        logger.info(f"Env: {sys.executable}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        logger.debug(traceback.format_exc())
        return

if __name__ == "__main__":
    main()
