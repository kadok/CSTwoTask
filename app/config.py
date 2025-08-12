import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_LINK = os.getenv("DB_LINK")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
