import pytest
from fastapi.testclient import TestClient
from src.api.main import app
from src.api.config import get_settings
import tempfile
from pathlib import Path

@pytest.fixture(autouse=True)
def setup_test_env():
    """Configure l'environnement de test"""
    # Utiliser un répertoire temporaire pour les tests
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        settings = get_settings()
        settings.CACHE_DIR = temp_path
        settings.DB_PATH = temp_path / "test_cache.json"
        yield

@pytest.fixture
def client():
    """Client de test FastAPI"""
    with TestClient(app) as test_client:
        yield test_client
