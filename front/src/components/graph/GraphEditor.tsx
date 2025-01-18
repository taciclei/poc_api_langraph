import React, { useCallback, useState } from 'react'
import ReactFlow, {
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  Edge,
  Node
} from 'reactflow'
import 'reactflow/dist/style.css'
import { Box, Paper, Typography } from '@mui/material'
import { NodeData, EdgeData } from '../../types/graph'
import CustomNode from './CustomNode'
import NodeConfigPanel from './NodeConfigPanel'

const nodeTypes = {
  custom: CustomNode,
}

interface GraphEditorProps {
  initialNodes?: Node<NodeData>[]
  initialEdges?: Edge<EdgeData>[]
  onSave?: (nodes: Node<NodeData>[], edges: Edge<EdgeData>[]) => void
}

export const GraphEditor: React.FC<GraphEditorProps> = ({
  initialNodes = [],
  initialEdges = [],
  onSave
}) => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes)
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges)
  const [selectedNode, setSelectedNode] = useState<Node<NodeData> | null>(null)

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  )

  const onNodeClick = useCallback((event: React.MouseEvent, node: Node) => {
    setSelectedNode(node)
  }, [])

  const handleSave = useCallback(() => {
    onSave?.(nodes, edges)
  }, [nodes, edges, onSave])

  const handleNodeConfigUpdate = useCallback((nodeId: string, config: any) => {
    setNodes((nds) =>
      nds.map((node) =>
        node.id === nodeId
          ? { ...node, data: { ...node.data, config } }
          : node
      )
    )
  }, [])

  return (
    <Box sx={{ display: 'flex', height: '100vh' }}>
      <Box sx={{ flex: 1, position: 'relative' }}>
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          onNodeClick={onNodeClick}
          nodeTypes={nodeTypes}
          fitView
        >
          <Background />
          <Controls />
          <MiniMap />
        </ReactFlow>
      </Box>
      {selectedNode && (
        <Paper
          sx={{
            width: 300,
            p: 2,
            height: '100%',
            overflowY: 'auto'
          }}
        >
          <Typography variant="h6" gutterBottom>
            Node Configuration
          </Typography>
          <NodeConfigPanel
            node={selectedNode}
            onUpdate={(config) => handleNodeConfigUpdate(selectedNode.id, config)}
          />
        </Paper>
      )}
    </Box>
  )
}

export default GraphEditor
