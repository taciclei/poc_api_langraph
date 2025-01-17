from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # LLM settings
    LLM_MODEL: str = "gpt-3.5-turbo"
    LLM_API_KEY: Optional[str] = None
    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 1000
    
    # Cache settings
    CACHE_TTL: int = 3600  # 1 hour
    
    # API settings
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()
