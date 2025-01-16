from typing import Dict, List
from fastapi import HTTPException
from .node_service import NodeService
from .edge_service import EdgeService

class ValidationService:
    @staticmethod
    def validate_graph_structure(graph_id: str) -> Dict:
        nodes = NodeService.list_nodes(graph_id)
        edges = EdgeService.list_edges(graph_id)
        
        # Vérifier que le graphe n'est pas vide
        if not nodes:
            raise HTTPException(
                status_code=400,
                detail="Graph must contain at least one node"
            )
            
        # Vérifier la connectivité
        node_ids = {node["_id"] for node in nodes}
        for edge in edges:
            if edge["source_id"] not in node_ids or edge["target_id"] not in node_ids:
                raise HTTPException(
                    status_code=400,
                    detail=f"Edge references non-existent node"
                )
        
        # Vérifier les cycles
        def has_cycle(graph: Dict[str, List[str]], node: str, visited: set, path: set) -> bool:
            visited.add(node)
            path.add(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if has_cycle(graph, neighbor, visited, path):
                        return True
                elif neighbor in path:
                    return True
                    
            path.remove(node)
            return False
            
        # Construire le graphe
        graph = {}
        for edge in edges:
            if edge["source_id"] not in graph:
                graph[edge["source_id"]] = []
            graph[edge["source_id"]].append(edge["target_id"])
            
        # Vérifier les cycles
        visited = set()
        path = set()
        
        for node in nodes:
            if node["_id"] not in visited:
                if has_cycle(graph, node["_id"], visited, path):
                    raise HTTPException(
                        status_code=400,
                        detail="Graph contains cycles"
                    )
                    
        return {"valid": True, "message": "Graph structure is valid"}
