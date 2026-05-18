from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    SHOP_ID: int
    SECRET_KEY: SecretStr
    CORE_URL: str
    BOT_URL: str

    SECRET_KEY_FOR_JWT: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()