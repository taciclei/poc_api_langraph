import React, { useCallback, useRef } from 'react';
import ReactFlow, {
  Background,
  Controls,
  Connection,
  useNodesState,
  useEdgesState,
  addEdge,
  useReactFlow,
  Node,
  ReactFlowInstance,
} from 'reactflow';
import 'reactflow/dist/style.css';

import { Box } from '@mui/material';
import { Toolbar } from '../../components/graph-editor/Toolbar';
import { NodePalette } from '../../components/graph-editor/palette/NodePalette';
import { PropertiesPanel } from '../../components/graph-editor/properties/PropertiesPanel';
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
  const reactFlowWrapper = useRef<HTMLDivElement>(null);
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [selectedNode, setSelectedNode] = React.useState<Node | null>(null);
  const { zoomIn, zoomOut, fitView, project } = useReactFlow();

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges],
  );

  const onDragOver = useCallback((event: React.DragEvent) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  }, []);

  const onDrop = useCallback(
    (event: React.DragEvent) => {
      event.preventDefault();

      if (reactFlowWrapper.current) {
        const type = event.dataTransfer.getData('application/reactflow');
        const position = project({
          x: event.clientX - reactFlowWrapper.current.getBoundingClientRect().left,
          y: event.clientY - reactFlowWrapper.current.getBoundingClientRect().top,
        });

        const newNode: CustomNode = {
          id: `${type}-${Date.now()}`,
          type: 'default',
          position,
          data: { label: `${type} node`, type },
        };

        setNodes((nds) => nds.concat(newNode));
      }
    },
    [project, setNodes],
  );

  const onNodeClick = useCallback(
    (_: React.MouseEvent, node: Node) => {
      setSelectedNode(node);
    },
    [setSelectedNode],
  );

  const onPaneClick = useCallback(() => {
    setSelectedNode(null);
  }, [setSelectedNode]);

  const handleNodeUpdate = useCallback(
    (nodeId: string, data: any) => {
      setNodes((nds) =>
        nds.map((node) => {
          if (node.id === nodeId) {
            return {
              ...node,
              data,
            };
          }
          return node;
        }),
      );
    },
    [setNodes],
  );

  return (
    <Box sx={{ display: 'flex', width: '100%', height: '100%' }}>
      <NodePalette />
      <Box
        ref={reactFlowWrapper}
        sx={{ flex: 1, height: '100%' }}
        onDragOver={onDragOver}
        onDrop={onDrop}
      >
        <Toolbar
          onSave={() => console.log('Saving graph:', { nodes, edges })}
          onRun={() => console.log('Running graph')}
          onZoomIn={zoomIn}
          onZoomOut={zoomOut}
          onFitView={fitView}
          onDelete={() => {
            setNodes((nds) => nds.filter((node) => !node.selected));
            setEdges((eds) => eds.filter((edge) => !edge.selected));
          }}
        />
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          onNodeClick={onNodeClick}
          onPaneClick={onPaneClick}
          nodeTypes={nodeTypes}
          fitView
        >
          <Background />
          <Controls />
        </ReactFlow>
      </Box>
      <PropertiesPanel selectedNode={selectedNode} onNodeUpdate={handleNodeUpdate} />
    </Box>
  );
};
