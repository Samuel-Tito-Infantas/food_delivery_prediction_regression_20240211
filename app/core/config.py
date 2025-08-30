from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODEL_PATH: str
    APP_NAME: str
    APP_VERSION: str

    class Config:
        env_file = ".env"


# Create a single settings instance to be used across the app
settings = Settings()
