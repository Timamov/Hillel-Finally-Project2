from pydantic_settings import BaseSettings
from functools import lru_cache
class Settings(BaseSettings):
    POSTGRES_DB = str
    POSTGRES_USER = str
    POSTGRES_PASSWORD = str
    POSTGRES_PORT = int
    POSTGRES_HOST = str

   

@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()