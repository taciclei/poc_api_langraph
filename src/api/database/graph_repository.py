from typing import List, Optional, Dict, Any
from pathlib import Path
import json
import uuid
from ..models.graph import Graph
from ..config import get_settings

settings = get_settings()

class GraphRepository:
    def __init__(self):
        self.db_path = settings.BASE_DIR / "data" / "graphs"
        self.db_path.mkdir(parents=True, exist_ok=True)

    def _generate_id(self) -> str:
        """Génère un ID unique pour un graphe"""
        return str(uuid.uuid4())

    def _get_graph_path(self, graph_id: str) -> Path:
        """Retourne le chemin du fichier pour un graphe"""
        return self.db_path / f"{graph_id}.json"

    def save(self, name: str, description: str, graph: Graph) -> Graph:
        """Sauvegarde un graphe"""
        graph_id = self._generate_id()
        graph_data = {
            "id": graph_id,
            "name": name,
            "description": description,
            "nodes": [node.model_dump() for node in graph.nodes],
            "edges": [edge.model_dump() for edge in graph.edges]
        }
        
        graph_path = self._get_graph_path(graph_id)
        with open(graph_path, 'w') as f:
            json.dump(graph_data, f, indent=2)
        
        return Graph(**graph_data)

    def get(self, graph_id: str) -> Optional[Graph]:
        """Récupère un graphe par son ID"""
        graph_path = self._get_graph_path(graph_id)
        if not graph_path.exists():
            return None
            
        with open(graph_path, 'r') as f:
            graph_data = json.load(f)
        
        return Graph(**graph_data)

    def list_all(self) -> List[Dict[str, Any]]:
        """Liste tous les graphes"""
        graphs = []
        for graph_file in self.db_path.glob("*.json"):
            with open(graph_file, 'r') as f:
                graph_data = json.load(f)
                graphs.append({
                    "id": graph_data["id"],
                    "name": graph_data["name"],
                    "description": graph_data["description"]
                })
        return graphs

    def delete(self, graph_id: str) -> bool:
        """Supprime un graphe"""
        graph_path = self._get_graph_path(graph_id)
        if not graph_path.exists():
            return False
            
        graph_path.unlink()
        return True

    def update(self, graph_id: str, graph_data: Dict[str, Any]) -> Optional[Graph]:
        """Met à jour un graphe"""
        existing_graph = self.get(graph_id)
        if not existing_graph:
            return None
            
        updated_data = {
            "id": graph_id,
            **graph_data
        }
        
        graph_path = self._get_graph_path(graph_id)
        with open(graph_path, 'w') as f:
            json.dump(updated_data, f, indent=2)
        
        return Graph(**updated_data)
