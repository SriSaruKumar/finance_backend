from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    FIREBASE_CREDENTIALS: str = "serviceAccountKey.json"

    class Config:
        env_file = ".env"

settings = Settings()
