import React from 'react';
import ReactFlow, { 
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState
} from 'reactflow';
import 'reactflow/dist/style.css';

interface GraphEditorProps {
  initialNodes?: any[];
  initialEdges?: any[];
  onSave?: (nodes: any[], edges: any[]) => void;
}

export const GraphEditor: React.FC<GraphEditorProps> = ({
  initialNodes = [],
  initialEdges = [],
  onSave
}) => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const handleSave = () => {
    onSave?.(nodes, edges);
  };

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
      >
        <Background />
        <Controls />
        <MiniMap />
      </ReactFlow>
      {onSave && (
        <button
          onClick={handleSave}
          style={{
            position: 'absolute',
            right: 10,
            top: 10,
            zIndex: 4,
          }}
        >
          Save Graph
        </button>
      )}
    </div>
  );
};
