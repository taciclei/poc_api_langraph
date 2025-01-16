"""Execution manager for handling graph executions."""
from typing import Dict, Any, Optional
from uuid import UUID

from src.api.models.execution import (
    Execution,
    ExecutionStatus,
    NodeExecutionResult,
    NodeExecutionStatus
)
from src.api.models.graph import Graph
from datetime import datetime


class ExecutionManager:
    """Manages the execution of a graph."""

    def __init__(self, graph: Graph):
        """Initialize execution manager.
        
        Args:
            graph: The graph to execute
        """
        self.graph = graph
        self._execution_cache: Dict[UUID, Any] = {}

    async def execute(self, execution: Execution) -> Execution:
        """Execute the graph.
        
        Args:
            execution: Execution details
            
        Returns:
            Updated execution with results
        """
        try:
            execution.status = ExecutionStatus.RUNNING
            
            # Topological sort for execution order
            sorted_nodes = self._topological_sort()
            
            # Execute nodes in order
            for node in sorted_nodes:
                node_result = await self._execute_node(node, execution.input_data)
                execution.node_results.append(node_result)
                
                if node_result.status == NodeExecutionStatus.FAILED:
                    execution.status = ExecutionStatus.FAILED
                    execution.error = f"Node {node.id} failed: {node_result.error}"
                    break
            
            if execution.status != ExecutionStatus.FAILED:
                execution.status = ExecutionStatus.COMPLETED
                execution.output_data = self._collect_outputs(execution.node_results)
            
        except Exception as e:
            execution.status = ExecutionStatus.FAILED
            execution.error = str(e)
        
        execution.end_time = datetime.utcnow()
        return execution

    def _topological_sort(self) -> list:
        """Perform topological sort on graph nodes."""
        # Implementation of topological sort
        # TODO: Implement actual topological sort
        return list(self.graph.nodes)

    async def _execute_node(self, node: Any, input_data: Dict[str, Any]) -> NodeExecutionResult:
        """Execute a single node.
        
        Args:
            node: Node to execute
            input_data: Input data for the node
            
        Returns:
            Execution result for the node
        """
        result = NodeExecutionResult(
            node_id=node.id,
            status=NodeExecutionStatus.RUNNING,
            start_time=datetime.utcnow()
        )
        
        try:
            # TODO: Implement actual node execution
            result.output = {"dummy": "output"}
            result.status = NodeExecutionStatus.COMPLETED
        except Exception as e:
            result.status = NodeExecutionStatus.FAILED
            result.error = str(e)
        
        result.end_time = datetime.utcnow()
        return result

    def _collect_outputs(self, node_results: list[NodeExecutionResult]) -> Dict[str, Any]:
        """Collect outputs from all completed nodes.
        
        Args:
            node_results: List of node execution results
            
        Returns:
            Combined output data
        """
        outputs = {}
        for result in node_results:
            if result.status == NodeExecutionStatus.COMPLETED and result.output:
                outputs[str(result.node_id)] = result.output
        return outputs