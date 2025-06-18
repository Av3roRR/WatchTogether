from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_DRIVER: str
    DATABASE_URL: str
    
    SECRET_KEY: str
    HASH_ALGO: str
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()