from os import getenv
import os
from typing import Optional, Any
from dotenv import load_dotenv
from pydantic import BaseSettings, \
    PostgresDsn, validator

# Loading .env file
load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Symphly Talk"
    API_VERSION: str = "/api/v1"

    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str]) -> Any:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            password=getenv("POSTGRES_PASSWORD"),
            host=getenv("POSTGRES_HOST"),
            port=getenv("POSTGRES_PORT"),
            path=f"/{getenv('POSTGRES_DB') or ''}"
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
