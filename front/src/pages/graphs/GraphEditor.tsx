import { Box, Paper, SpeedDial, SpeedDialAction, Typography } from '@mui/material';
import {
  Add as AddIcon,
  Save as SaveIcon,
  PlayArrow as PlayIcon,
  SmartToy as LLMIcon,
  Description as PromptIcon,
  Build as ToolIcon,
  Output as OutputIcon,
} from '@mui/icons-material';
import ReactFlow, {
  Background,
  Controls,
  Panel,
  applyEdgeChanges,
  applyNodeChanges,
  addEdge,
  Connection,
  Edge,
  Node,
  NodeChange,
  EdgeChange,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { useCallback, useState } from 'react';
import { useParams } from 'react-router-dom';
import BaseNode from '../../components/nodes/BaseNode';
import NodeConfigPanel from '../../components/panels/NodeConfigPanel';
import { LangGraphNode, LangGraphEdge } from '../../types/graph';

const nodeTypes = {
  base: BaseNode,
};

const initialNodes: LangGraphNode[] = [
  {
    id: '1',
    type: 'base',
    position: { x: 100, y: 100 },
    data: { label: 'LLM Node', type: 'llm', config: {} },
  },
];

const initialEdges: LangGraphEdge[] = [];

const flowStyles = {
  background: '#1E1E1E',
};

const edgeOptions = {
  type: 'smoothstep',
  style: {
    stroke: 'rgba(255, 255, 255, 0.3)',
    strokeWidth: 2,
  },
  markerEnd: {
    type: 'arrowclosed',
    color: 'rgba(255, 255, 255, 0.3)',
  },
};

export const GraphEditor = () => {
  const { id } = useParams();
  const [nodes, setNodes] = useState<LangGraphNode[]>(initialNodes);
  const [edges, setEdges] = useState<LangGraphEdge[]>(initialEdges);
  const [selectedNode, setSelectedNode] = useState<LangGraphNode | null>(null);

  const onNodesChange = useCallback(
    (changes: NodeChange[]) => {
      setNodes((nds) => applyNodeChanges(changes, nds));
      
      const positionChange = changes.find(
        (change) => change.type === 'position' && change.id === selectedNode?.id
      );
      if (positionChange && selectedNode) {
        setSelectedNode((prev) =>
          prev ? { ...prev, position: positionChange.position! } : null
        );
      }
    },
    [selectedNode]
  );

  const onEdgesChange = useCallback(
    (changes: EdgeChange[]) => setEdges((eds) => applyEdgeChanges(changes, eds)),
    []
  );

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    []
  );

  const onNodeClick = useCallback(
    (_: React.MouseEvent, node: Node) => {
      const fullNode = nodes.find((n) => n.id === node.id);
      if (fullNode) {
        setSelectedNode(fullNode);
      }
    },
    [nodes]
  );

  const addNode = (type: 'llm' | 'prompt' | 'tool' | 'output') => {
    const newNode: LangGraphNode = {
      id: `${Date.now()}`,
      type: 'base',
      position: { x: 100, y: 100 },
      data: { label: `New ${type}`, type, config: {} },
    };
    setNodes((nds) => [...nds, newNode]);
  };

  const updateNode = useCallback(
    (nodeId: string, updates: Partial<LangGraphNode>) => {
      setNodes((nds) =>
        nds.map((node) =>
          node.id === nodeId ? { ...node, ...updates } : node
        )
      );
      setSelectedNode((prev) =>
        prev?.id === nodeId ? { ...prev, ...updates } : prev
      );
    },
    []
  );

  return (
    <Box sx={{ height: 'calc(100vh - 100px)' }}>
      <Paper
        sx={{
          height: '100%',
          position: 'relative',
          overflow: 'hidden',
          backgroundColor: 'transparent',
          backgroundImage: 'radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.03) 0%, transparent 100%)',
        }}
      >
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          onNodeClick={onNodeClick}
          nodeTypes={nodeTypes}
          defaultEdgeOptions={edgeOptions}
          fitView
          style={flowStyles}
        >
          <Background
            color="rgba(255, 255, 255, 0.05)"
            gap={24}
            size={1}
          />
          <Controls
            style={{
              backgroundColor: 'rgba(0, 0, 0, 0.8)',
              borderRadius: '8px',
              padding: '4px',
            }}
          />
          <Panel
            position="top-left"
            style={{
              margin: '10px',
              padding: '8px 12px',
              backgroundColor: 'rgba(0, 0, 0, 0.8)',
              borderRadius: '8px',
            }}
          >
            <Typography
              variant="h6"
              sx={{
                color: 'rgba(255, 255, 255, 0.9)',
                fontWeight: 600,
              }}
            >
              {id ? `Graph: ${id}` : 'New Graph'}
            </Typography>
          </Panel>
        </ReactFlow>
        <SpeedDial
          ariaLabel="Graph Actions"
          sx={{
            position: 'absolute',
            bottom: 16,
            right: 16,
            '& .MuiSpeedDial-fab': {
              backgroundColor: 'rgba(0, 0, 0, 0.8)',
              '&:hover': {
                backgroundColor: 'rgba(0, 0, 0, 0.9)',
              },
            },
          }}
          icon={<AddIcon />}
        >
          <SpeedDialAction
            icon={<LLMIcon />}
            tooltipTitle="Add LLM"
            onClick={() => addNode('llm')}
          />
          <SpeedDialAction
            icon={<PromptIcon />}
            tooltipTitle="Add Prompt"
            onClick={() => addNode('prompt')}
          />
          <SpeedDialAction
            icon={<ToolIcon />}
            tooltipTitle="Add Tool"
            onClick={() => addNode('tool')}
          />
          <SpeedDialAction
            icon={<OutputIcon />}
            tooltipTitle="Add Output"
            onClick={() => addNode('output')}
          />
          <SpeedDialAction
            icon={<SaveIcon />}
            tooltipTitle="Save Graph"
            onClick={() => console.log('Save graph')}
          />
          <SpeedDialAction
            icon={<PlayIcon />}
            tooltipTitle="Execute Graph"
            onClick={() => console.log('Execute graph')}
          />
        </SpeedDial>
      </Paper>
      <NodeConfigPanel
        node={selectedNode}
        open={!!selectedNode}
        onClose={() => setSelectedNode(null)}
        onUpdate={updateNode}
      />
    </Box>
  );
};
