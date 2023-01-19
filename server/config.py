from pydantic import BaseSettings
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    FASTAPI_ROOT_PATH: str = ""
    DEBUG: bool = True
    SECRET_KEY: str = "claveSecreta12"
    DATABASE_URI: str = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
    VITE_API_BASE_URL: str

    class Config:
        case_sensitive = True
        env_file = "../.env"


settings = Settings(_env_file="../.env" + (".production" if os.getenv("PROD") else ""))
