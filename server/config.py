from pydantic import BaseSettings
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    FASTAPI_ROOT_PATH: str = ""
    DEBUG: bool
    DATABASE_URI: str

    class Config:
        case_sensitive = True
        env_file = "../.env"


settings = Settings(_env_file="../.env" + (".production" if os.getenv("PROD") else ""))
