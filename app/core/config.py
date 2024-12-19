from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    WATI_API_KEY: str
    WATI_API_URL: str
    LOG_LEVEL: str = "INFO"
    service_host: str = "0.0.0.0"
    service_port: int = 8000
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-3.5-turbo"

    class Config:
        env_file = ".env"

settings = Settings() 