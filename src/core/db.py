from pathlib import Path
from tinydb import TinyDB

class DBConfig:
    _db = None
    _db_path = Path("data/db.json")

    @classmethod
    def connect(cls):
        # Créer le dossier data s'il n'existe pas
        cls._db_path.parent.mkdir(exist_ok=True)
        cls._db = TinyDB(cls._db_path)

    @classmethod
    def close(cls):
        if cls._db:
            cls._db.close()

    @classmethod
    def get_db(cls) -> TinyDB:
        if not cls._db:
            cls.connect()
        return cls._db