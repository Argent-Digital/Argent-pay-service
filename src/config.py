from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    SHOP_ID: int
    SECRET_KEY: SecretStr

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()