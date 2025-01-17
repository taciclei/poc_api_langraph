from typing import List, Optional, Dict, Any
from datetime import datetime
from src.api.models.graph import Graph, GraphCreate, GraphUpdate

class GraphRepository:
    def __init__(self):
        self.graphs: Dict[str, Graph] = {}

    async def create(self, graph: Graph) -> Graph:
        """Crée un nouveau graphe"""
        self.graphs[graph.id] = graph
        return graph

    async def get(self, graph_id: str) -> Optional[Graph]:
        """Récupère un graphe par son ID"""
        return self.graphs.get(graph_id)

    async def update(self, graph_id: str, data: Dict[str, Any]) -> Optional[Graph]:
        """Met à jour un graphe existant"""
        if graph_id not in self.graphs:
            return None
        
        graph = self.graphs[graph_id]
        updated_graph = graph.model_copy(update=data)
        self.graphs[graph_id] = updated_graph
        return updated_graph

    async def delete(self, graph_id: str) -> bool:
        """Supprime un graphe"""
        if graph_id in self.graphs:
            del self.graphs[graph_id]
            return True
        return False

    async def list(self, skip: int = 0, limit: int = 10) -> List[Graph]:
        """Liste tous les graphes avec pagination"""
        graphs = list(self.graphs.values())
        return graphs[skip:skip + limit]
