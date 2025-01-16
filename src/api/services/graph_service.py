from typing import Dict, List, Optional
from tinydb import TinyDB, Query
import uuid

class GraphService:
    def __init__(self):
        self.db = TinyDB('db.json')
        self.graphs = self.db.table('graphs')

    def create_graph(self, name: str, description: str, nodes: List[str], edges: List[Dict]) -> Dict:
        """Create a new graph"""
        graph_id = str(uuid.uuid4())
        graph = {
            "id": graph_id,
            "name": name,
            "description": description,
            "nodes": nodes,
            "edges": edges
        }
        self.graphs.insert(graph)
        return graph

    def get_graph(self, graph_id: str) -> Optional[Dict]:
        """Get a graph by ID"""
        Graph = Query()
        result = self.graphs.search(Graph.id == graph_id)
        return result[0] if result else None

    def delete_graph(self, graph_id: str) -> bool:
        """Delete a graph by ID"""
        Graph = Query()
        return bool(self.graphs.remove(Graph.id == graph_id))

    def list_graphs(self) -> List[Dict]:
        """List all graphs"""
        return self.graphs.all()
