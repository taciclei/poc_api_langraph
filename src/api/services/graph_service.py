from typing import List, Optional, Dict, Any
from ..models.graph import Graph, GraphCreate, GraphUpdate

class GraphService:
    def __init__(self):
        # Initialiser avec une base de données en mémoire pour l'exemple
        self.graphs: Dict[str, Graph] = {}

    async def create_graph(self, graph_data: Dict[str, Any]) -> Graph:
        """Crée un nouveau graphe"""
        graph = Graph(**graph_data)
        self.graphs[graph.id] = graph
        return graph

    async def get_graph(self, graph_id: str) -> Optional[Graph]:
        """Récupère un graphe par son ID"""
        return self.graphs.get(graph_id)

    async def update_graph(self, graph_id: str, graph_data: Dict[str, Any]) -> Optional[Graph]:
        """Met à jour un graphe existant"""
        if graph_id not in self.graphs:
            return None
        updated_graph = Graph(**{**self.graphs[graph_id].dict(), **graph_data})
        self.graphs[graph_id] = updated_graph
        return updated_graph

    async def delete_graph(self, graph_id: str) -> bool:
        """Supprime un graphe"""
        if graph_id in self.graphs:
            del self.graphs[graph_id]
            return True
        return False

    async def list_graphs(self, skip: int = 0, limit: int = 10) -> List[Graph]:
        """Liste tous les graphes avec pagination"""
        return list(self.graphs.values())[skip:skip + limit]

# Créer une instance unique du service
graph_service = GraphService()
