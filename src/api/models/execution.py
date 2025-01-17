from pydantic import BaseModel
from typing import Dict, Any, Optional
from datetime import datetime
from enum import Enum

class ExecutionStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class ExecutionBase(BaseModel):
    graph_id: str
    inputs: Dict[str, Any] = {}
    status: ExecutionStatus = ExecutionStatus.PENDING
    outputs: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

class ExecutionCreate(ExecutionBase):
    pass

class ExecutionUpdate(BaseModel):
    status: Optional[ExecutionStatus] = None
    outputs: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

class Execution(ExecutionBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
