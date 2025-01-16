from typing import Dict, List, Optional
import uuid
from fastapi import HTTPException
from langgraph.graph import Graph
from .base_db_service import BaseDBService

class GraphService(BaseDBService):
    table_name = "graphs"

    @classmethod
    def create_graph(cls, graph_data: Dict) -> Dict:
        graph_data["_id"] = str(uuid.uuid4())
        return cls.create(graph_data)

    @classmethod
    def get_graph(cls, graph_id: str) -> Dict:
        graph = cls.get_by_id(graph_id)
        if not graph:
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Graph not found"
                }]
            })
        return graph

    @classmethod
    def list_graphs(cls, status: Optional[str] = None, skip: int = 0, limit: int = 10) -> List[Dict]:
        filter_dict = {"status": status} if status else None
        return cls.list(filter_dict, skip, limit)

    @classmethod
    def update_graph(cls, graph_id: str, graph_data: Dict) -> Dict:
        graph = cls.update(graph_id, graph_data)
        if not graph:
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Graph not found"
                }]
            })
        return graph

    @classmethod
    def delete_graph(cls, graph_id: str) -> None:
        if not cls.delete(graph_id):
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Graph not found"
                }]
            })