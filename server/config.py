from pydantic import BaseSettings, validator
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    # Secrets
    DB_PASS: str = ''

    FASTAPI_ROOT_PATH: str = ""
    DEBUG: bool
    DATABASE_URI: str

    class Config:
        case_sensitive = True

    @validator('*', pre=True)
    def val_func(cls, v, values, config):
        for k in values:
            v = v.replace(f"{{{k}}}", str(values[k]))
        return v


settings = Settings(_env_file="../.env" + (".production" if os.getenv("PROD") else ""), _secrets_dir="../secrets")
