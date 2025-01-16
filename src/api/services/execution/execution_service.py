"""Service for managing graph executions."""
from typing import List, Optional
from uuid import UUID

from src.api.models.execution import (
    Execution,
    ExecutionCreate,
    ExecutionUpdate,
    ExecutionFilter
)
from src.api.services.graph_service import GraphService
from src.api.services.execution.execution_manager import ExecutionManager


class ExecutionService:
    """Service for managing graph executions."""

    def __init__(self, graph_service: GraphService):
        """Initialize execution service.
        
        Args:
            graph_service: Service for managing graphs
        """
        self.graph_service = graph_service
        self._executions: List[Execution] = []

    async def create_execution(self, execution_create: ExecutionCreate) -> Execution:
        """Create and start a new execution.
        
        Args:
            execution_create: Execution creation details
            
        Returns:
            Created execution
        """
        # Get the graph
        graph = await self.graph_service.get_graph(execution_create.graph_id)
        if not graph:
            raise ValueError(f"Graph {execution_create.graph_id} not found")

        # Create execution
        execution = Execution(
            graph_id=graph.id,
            input_data=execution_create.input_data,
            metadata=execution_create.metadata
        )
        
        # Execute graph
        manager = ExecutionManager(graph)
        execution = await manager.execute(execution)
        
        # Store execution
        self._executions.append(execution)
        
        return execution

    async def get_execution(self, execution_id: UUID) -> Optional[Execution]:
        """Get execution by ID.
        
        Args:
            execution_id: ID of the execution
            
        Returns:
            Execution if found, None otherwise
        """
        for execution in self._executions:
            if execution.id == execution_id:
                return execution
        return None

    async def list_executions(self, filter_params: ExecutionFilter) -> List[Execution]:
        """List executions with optional filtering.
        
        Args:
            filter_params: Filter parameters
            
        Returns:
            List of matching executions
        """
        executions = self._executions
        
        if filter_params.graph_id:
            executions = [e for e in executions if e.graph_id == filter_params.graph_id]
        
        if filter_params.status:
            executions = [e for e in executions if e.status == filter_params.status]
        
        if filter_params.start_time_after:
            executions = [e for e in executions if e.start_time >= filter_params.start_time_after]
        
        if filter_params.start_time_before:
            executions = [e for e in executions if e.start_time <= filter_params.start_time_before]
        
        return executions

    async def update_execution(
        self, execution_id: UUID, execution_update: ExecutionUpdate
    ) -> Optional[Execution]:
        """Update execution details.
        
        Args:
            execution_id: ID of the execution to update
            execution_update: Update details
            
        Returns:
            Updated execution if found, None otherwise
        """
        execution = await self.get_execution(execution_id)
        if not execution:
            return None

        # Update fields
        for field, value in execution_update.dict(exclude_unset=True).items():
            setattr(execution, field, value)

        return execution