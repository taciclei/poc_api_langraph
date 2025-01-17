from typing import List, Optional, Dict, Any
from datetime import datetime
from src.api.models.execution import Execution, ExecutionCreate, ExecutionUpdate

class ExecutionRepository:
    def __init__(self):
        self.executions: Dict[str, Execution] = {}

    async def create(self, execution: Execution) -> Execution:
        """Crée une nouvelle exécution"""
        self.executions[execution.id] = execution
        return execution

    async def get(self, execution_id: str) -> Optional[Execution]:
        """Récupère une exécution par son ID"""
        return self.executions.get(execution_id)

    async def update(self, execution_id: str, data: Dict[str, Any]) -> Optional[Execution]:
        """Met à jour une exécution existante"""
        if execution_id not in self.executions:
            return None
        
        execution = self.executions[execution_id]
        updated_execution = execution.model_copy(update=data)
        self.executions[execution_id] = updated_execution
        return updated_execution

    async def delete(self, execution_id: str) -> bool:
        """Supprime une exécution"""
        if execution_id in self.executions:
            del self.executions[execution_id]
            return True
        return False

    async def list(
        self,
        graph_id: Optional[str] = None,
        status: Optional[str] = None,
        skip: int = 0,
        limit: int = 10
    ) -> List[Execution]:
        """Liste toutes les exécutions avec filtres et pagination"""
        executions = list(self.executions.values())
        
        if graph_id:
            executions = [e for e in executions if e.graph_id == graph_id]
        if status:
            executions = [e for e in executions if e.status == status]
            
        return executions[skip:skip + limit]
