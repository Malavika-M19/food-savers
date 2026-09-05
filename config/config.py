import os
from dotenv import load_dotenv

#Load values from .env file
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "https://foodsavers.app/")
#HEADLESS = os.getenv("HEADLESS","false").lower() == "true"
USERNAME = os.getenv("FS_USERNAME",None)
PASSWORD = os.getenv("FS_PASSWORD",None)