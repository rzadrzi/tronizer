
import os

from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.getcwd(), ".env")
print(DOTENV)


class Settings(BaseSettings):
    MODE: str
    PUBLIC_KEY: str
    PRIVATE_KEY: str
    TRONGRID: str
    MONGO_LOCAL_URI: str
    MONGO_DOCKER_URI: str

    model_config = SettingsConfigDict(env_file=DOTENV)
