from typing import List, Dict, Optional
from tinydb import Query
from ...core.db import DBConfig

class BaseDBService:
    table_name: str = None

    @classmethod
    def get_table(cls):
        return DBConfig.get_db().table(cls.table_name)

    @classmethod
    def create(cls, data: Dict) -> Dict:
        table = cls.get_table()
        doc_id = table.insert(data)
        return {**data, "doc_id": doc_id}

    @classmethod
    def get_by_id(cls, id: str) -> Optional[Dict]:
        table = cls.get_table()
        Q = Query()
        return table.get(Q._id == id)

    @classmethod
    def list(cls, filter_dict: Dict = None, skip: int = 0, limit: int = 10) -> List[Dict]:
        table = cls.get_table()
        results = table.all()
        
        if filter_dict:
            Q = Query()
            for key, value in filter_dict.items():
                results = [r for r in results if r.get(key) == value]
        
        return results[skip:skip + limit]

    @classmethod
    def update(cls, id: str, data: Dict) -> Optional[Dict]:
        table = cls.get_table()
        Q = Query()
        table.update(data, Q._id == id)
        return cls.get_by_id(id)

    @classmethod
    def delete(cls, id: str) -> bool:
        table = cls.get_table()
        Q = Query()
        return table.remove(Q._id == id) != []