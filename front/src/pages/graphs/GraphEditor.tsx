import React, { useCallback } from 'react';
import ReactFlow, {
  Background,
  Controls,
  Node,
  Edge,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  useReactFlow,
} from 'reactflow';
import 'reactflow/dist/style.css';

import { Box } from '@mui/material';
import { Toolbar } from '../../components/graph-editor/Toolbar';
import { CustomNodes } from '../../components/graph-editor/CustomNodes';
import { CustomNode } from '../../types/graph';

const initialNodes: CustomNode[] = [
  {
    id: '1',
    type: 'default',
    position: { x: 250, y: 100 },
    data: { label: 'Input Node', type: 'input' },
  },
];

const nodeTypes = CustomNodes;

export const GraphEditor: React.FC = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const { zoomIn, zoomOut, fitView } = useReactFlow();

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges],
  );

  const handleSave = useCallback(() => {
    // TODO: Implement save functionality
    console.log('Saving graph:', { nodes, edges });
  }, [nodes, edges]);

  const handleRun = useCallback(() => {
    // TODO: Implement run functionality
    console.log('Running graph');
  }, []);

  const handleDelete = useCallback(() => {
    // TODO: Implement delete functionality
    setNodes((nds) => nds.filter((node) => !node.selected));
    setEdges((eds) => eds.filter((edge) => !edge.selected));
  }, [setNodes, setEdges]);

  return (
    <Box sx={{ width: '100%', height: '100%', position: 'relative' }}>
      <Toolbar
        onSave={handleSave}
        onRun={handleRun}
        onZoomIn={() => zoomIn()}
        onZoomOut={() => zoomOut()}
        onFitView={() => fitView()}
        onDelete={handleDelete}
      />
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        fitView
      >
        <Background />
        <Controls />
      </ReactFlow>
    </Box>
  );
};
