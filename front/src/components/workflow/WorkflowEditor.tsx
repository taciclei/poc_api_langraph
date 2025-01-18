import React, { useCallback } from 'react';
import ReactFlow, {
  Background,
  Controls,
  Node,
  Edge,
  Connection,
  addEdge,
  useNodesState,
  useEdgesState,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { Box, Paper } from '@mui/material';
import CustomNode from './CustomNode';

const nodeTypes = {
  custom: CustomNode,
};

interface WorkflowEditorProps {
  initialNodes?: Node[];
  initialEdges?: Edge[];
  onNodesChange?: (nodes: Node[]) => void;
  onEdgesChange?: (edges: Edge[]) => void;
  onNodeSelect?: (node: Node | null) => void;
  readonly?: boolean;
}

const WorkflowEditor: React.FC<WorkflowEditorProps> = ({
  initialNodes = [],
  initialEdges = [],
  onNodesChange: onNodesChangeCallback,
  onEdgesChange: onEdgesChangeCallback,
  onNodeSelect,
  readonly = false,
}) => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const handleNodesChange = useCallback(
    (changes: any) => {
      onNodesChange(changes);
      if (onNodesChangeCallback) {
        const updatedNodes = nodes.map(node => ({...node}));
        onNodesChangeCallback(updatedNodes);
      }
    },
    [nodes, onNodesChange, onNodesChangeCallback]
  );

  const handleEdgesChange = useCallback(
    (changes: any) => {
      onEdgesChange(changes);
      if (onEdgesChangeCallback) {
        const updatedEdges = edges.map(edge => ({...edge}));
        onEdgesChangeCallback(updatedEdges);
      }
    },
    [edges, onEdgesChange, onEdgesChangeCallback]
  );

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  const onNodeClick = useCallback(
    (_: React.MouseEvent, node: Node) => {
      if (onNodeSelect) {
        onNodeSelect(node);
      }
    },
    [onNodeSelect]
  );

  return (
    <Paper
      sx={{
        height: '70vh',
        width: '100%',
        bgcolor: 'background.default',
        borderRadius: 2,
        overflow: 'hidden',
      }}
    >
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={handleNodesChange}
        onEdgesChange={handleEdgesChange}
        onConnect={onConnect}
        onNodeClick={onNodeClick}
        nodeTypes={nodeTypes}
        fitView
        attributionPosition="bottom-right"
        nodesDraggable={!readonly}
        nodesConnectable={!readonly}
        elementsSelectable={!readonly}
      >
        <Background />
        <Controls />
      </ReactFlow>
    </Paper>
  );
};

export default WorkflowEditor;
