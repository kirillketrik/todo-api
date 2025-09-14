
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite://db.sqlite3"
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

def get_settings():
    print(settings)
    return settings
