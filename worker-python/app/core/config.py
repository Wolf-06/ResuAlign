import os
from  pathlib import Path
from typing import Optional
from pydantic import computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR= Path(__file__).resolve().parent.parent.parent.parent
ENV_FILE= BASE_DIR/".env"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE,case_sensitive=True,extra="ignore")

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int = 5432

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        path = f"/{self.DB_NAME}" if self.DB_NAME else ""

        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host="localhost",
            port=self.DB_PORT,
            path=path,
        ).unicode_string()
    
settings=Settings() # type: ignore // bcoz the pylance can't understand that the arguments are dynamically feeded

print(settings.DATABASE_URL)