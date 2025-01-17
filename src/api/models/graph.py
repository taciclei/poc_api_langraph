<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel

class Graph(BaseModel):
    __tablename__ = "graphs"

    name = Column(String, nullable=False, index=True)
    description = Column(Text)
    nodes = relationship("Node", back_populates="graph", cascade="all, delete-orphan")
    edges = relationship("Edge", back_populates="graph", cascade="all, delete-orphan")

class Node(BaseModel):
    __tablename__ = "nodes"

    graph_id = Column(Integer, ForeignKey("graphs.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    config = Column(JSON)
    position = Column(JSON)
    
    graph = relationship("Graph", back_populates="nodes")
    outgoing_edges = relationship("Edge", foreign_keys="Edge.source_id", back_populates="source")
    incoming_edges = relationship("Edge", foreign_keys="Edge.target_id", back_populates="target")

class Edge(BaseModel):
    __tablename__ = "edges"

    graph_id = Column(Integer, ForeignKey("graphs.id", ondelete="CASCADE"), nullable=False, index=True)
    source_id = Column(Integer, ForeignKey("nodes.id", ondelete="CASCADE"), nullable=False)
    target_id = Column(Integer, ForeignKey("nodes.id", ondelete="CASCADE"), nullable=False)
    config = Column(JSON)

    graph = relationship("Graph", back_populates="edges")
    source = relationship("Node", foreign_keys=[source_id], back_populates="outgoing_edges")
    target = relationship("Node", foreign_keys=[target_id], back_populates="incoming_edges")
=======
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Node(BaseModel):
    id: Optional[str] = None
    name: str
    type: str
    graph_id: Optional[str] = None
    properties: Optional[Dict[str, Any]] = {}

class Edge(BaseModel):
    id: Optional[str] = None
    source_id: str
    target_id: str
    graph_id: Optional[str] = None
    properties: Optional[Dict[str, Any]] = {}

class Graph(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    nodes: List[Node] = []
    edges: List[Edge] = []
    properties: Optional[Dict[str, Any]] = {}

class GraphResponse(BaseModel):
    id: str
    name: str
    description: str
    nodes: List[Node]
    edges: List[Edge]
    properties: Dict[str, Any] = {}
>>>>>>> release/1.1.0
