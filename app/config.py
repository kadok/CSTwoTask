import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
        Classe responsável por definir as constantes através do arquivo de propriedades.
    """
    DB_LINK = os.getenv("DB_LINK")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
