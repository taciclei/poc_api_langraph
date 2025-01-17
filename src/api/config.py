from pydantic_settings import BaseSettings
from typing import Optional, Literal
import os
from pathlib import Path
from enum import Enum

class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

class CacheType(str, Enum):
    TINYDB = "tinydb"
    REDIS = "redis"
    MEMORY = "memory"

class Settings(BaseSettings):
    # Chemins
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    CACHE_DIR: Path = BASE_DIR / "cache"
    DATA_DIR: Path = BASE_DIR / "data"
    
    # Configuration du cache
    CACHE_TYPE: CacheType = CacheType.TINYDB
    CACHE_DB_PATH: str = "cache.json"
    CACHE_TTL: int = 3600  # 1 heure par défaut
    DB_PATH: Path = CACHE_DIR / CACHE_DB_PATH
    
    # Configuration de la base de données
    DATABASE_URL: str = "sqlite:///./app.db"
    
    # Configuration des logs
    LOG_LEVEL: LogLevel = LogLevel.INFO
    
    # Clés API
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    MISTRAL_API_KEY: Optional[str] = None
    
    # Configuration LLM
    DEFAULT_MODEL: str = "gpt-4"
    MAX_RETRIES: int = 3
    REQUEST_TIMEOUT: int = 30
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        use_enum_values = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Créer les répertoires nécessaires
        self.CACHE_DIR.mkdir(parents=True, exist_ok=True)
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)
        # Mise à jour du DB_PATH après l'initialisation
        self.DB_PATH = self.CACHE_DIR / self.CACHE_DB_PATH

_settings = None

def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
