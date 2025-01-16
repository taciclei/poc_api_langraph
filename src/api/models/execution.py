"""Models for graph execution management."""
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional, List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ExecutionStatus(str, Enum):
    """Status of a graph execution."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class NodeExecutionStatus(str, Enum):
    """Status of a node execution within a graph."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class NodeExecutionResult(BaseModel):
    """Result of a single node execution."""
    node_id: UUID
    status: NodeExecutionStatus
    start_time: datetime
    end_time: Optional[datetime] = None
    output: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ExecutionCreate(BaseModel):
    """Model for creating a new execution."""
    graph_id: UUID
    input_data: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Execution(BaseModel):
    """Model representing a graph execution."""
    id: UUID = Field(default_factory=uuid4)
    graph_id: UUID
    status: ExecutionStatus = Field(default=ExecutionStatus.PENDING)
    start_time: datetime = Field(default_factory=datetime.utcnow)
    end_time: Optional[datetime] = None
    input_data: Dict[str, Any] = Field(default_factory=dict)
    output_data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    node_results: List[NodeExecutionResult] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        """Pydantic model configuration."""
        json_encoders = {
            UUID: str,
            datetime: lambda v: v.isoformat()
        }


class ExecutionUpdate(BaseModel):
    """Model for updating an execution."""
    status: Optional[ExecutionStatus] = None
    end_time: Optional[datetime] = None
    output_data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class ExecutionFilter(BaseModel):
    """Model for filtering executions."""
    graph_id: Optional[UUID] = None
    status: Optional[ExecutionStatus] = None
    start_time_after: Optional[datetime] = None
    start_time_before: Optional[datetime] = None