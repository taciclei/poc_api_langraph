"""Tests for execution service."""
import pytest
from uuid import UUID, uuid4
from datetime import datetime, timedelta

from src.api.models.execution import (
    Execution,
    ExecutionCreate,
    ExecutionUpdate,
    ExecutionFilter,
    ExecutionStatus
)
from src.api.services.execution.execution_service import ExecutionService
from src.api.services.graph_service import GraphService


@pytest.fixture
def graph_service():
    """Fixture for graph service."""
    return GraphService()


@pytest.fixture
def execution_service(graph_service):
    """Fixture for execution service."""
    return ExecutionService(graph_service)


@pytest.mark.asyncio
async def test_create_execution(execution_service, mocker):
    """Test creating a new execution."""
    # Mock graph service
    graph_id = uuid4()
    mocker.patch.object(
        execution_service.graph_service,
        "get_graph",
        return_value={"id": graph_id}
    )

    # Create execution
    execution_create = ExecutionCreate(
        graph_id=graph_id,
        input_data={"test": "data"}
    )
    
    execution = await execution_service.create_execution(execution_create)
    
    assert execution.graph_id == graph_id
    assert execution.status == ExecutionStatus.COMPLETED
    assert execution.input_data == {"test": "data"}
    assert execution.end_time is not None


@pytest.mark.asyncio
async def test_get_execution(execution_service):
    """Test getting an execution by ID."""
    # Create test execution
    execution = Execution(graph_id=uuid4())
    execution_service._executions.append(execution)
    
    # Get execution
    result = await execution_service.get_execution(execution.id)
    
    assert result == execution


@pytest.mark.asyncio
async def test_list_executions_with_filters(execution_service):
    """Test listing executions with filters."""
    # Create test executions
    graph_id = uuid4()
    now = datetime.utcnow()
    
    execution1 = Execution(
        graph_id=graph_id,
        status=ExecutionStatus.COMPLETED,
        start_time=now - timedelta(hours=2)
    )
    execution2 = Execution(
        graph_id=graph_id,
        status=ExecutionStatus.FAILED,
        start_time=now - timedelta(hours=1)
    )
    
    execution_service._executions.extend([execution1, execution2])
    
    # Test filters
    filter_params = ExecutionFilter(
        graph_id=graph_id,
        status=ExecutionStatus.COMPLETED,
        start_time_after=now - timedelta(hours=3)
    )
    
    results = await execution_service.list_executions(filter_params)
    
    assert len(results) == 1
    assert results[0] == execution1


@pytest.mark.asyncio
async def test_update_execution(execution_service):
    """Test updating an execution."""
    # Create test execution
    execution = Execution(graph_id=uuid4())
    execution_service._executions.append(execution)
    
    # Update execution
    update = ExecutionUpdate(status=ExecutionStatus.FAILED)
    result = await execution_service.update_execution(execution.id, update)
    
    assert result.status == ExecutionStatus.FAILED