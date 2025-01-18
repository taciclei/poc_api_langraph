import React, { useState, useEffect, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  Container,
  Paper,
  Box,
  Typography,
  Button,
  TextField,
  Drawer,
  IconButton,
  Divider,
  Alert,
} from '@mui/material';
import {
  Save as SaveIcon,
  PlayArrow as RunIcon,
  Close as CloseIcon,
  Add as AddIcon,
} from '@mui/icons-material';
import { Node, Edge, ReactFlowProvider } from 'reactflow';
import 'reactflow/dist/style.css';
import { useWorkflow } from '../../hooks/useWorkflow';
import WorkflowEditor from '../../components/workflow/WorkflowEditor';
import NodePalette from '../../components/workflow/NodePalette';
import NodeConfigPanel from '../../components/workflow/NodeConfigPanel';

const WorkflowEditPage: React.FC = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { getWorkflow, createWorkflow, updateWorkflow } = useWorkflow();

  const [workflow, setWorkflow] = useState({
    name: '',
    description: '',
    nodes: [] as Node[],
    edges: [] as Edge[],
  });
  const [selectedNode, setSelectedNode] = useState<Node | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isPaletteOpen, setIsPaletteOpen] = useState(true);

  useEffect(() => {
    const loadWorkflow = async () => {
      if (id) {
        try {
          const data = await getWorkflow(id);
          setWorkflow(data);
        } catch (err) {
          setError('Failed to load workflow');
        }
      }
    };
    loadWorkflow();
  }, [id, getWorkflow]);

  const handleSave = async () => {
    try {
      if (id) {
        await updateWorkflow(id, workflow);
      } else {
        const newWorkflow = await createWorkflow(workflow);
        navigate(`/workflows/${newWorkflow.id}`);
      }
    } catch (err) {
      setError('Failed to save workflow');
    }
  };

  const handleNodesChange = useCallback((nodes: Node[]) => {
    setWorkflow(prev => ({ ...prev, nodes }));
  }, []);

  const handleEdgesChange = useCallback((edges: Edge[]) => {
    setWorkflow(prev => ({ ...prev, edges }));
  }, []);

  const handleNodeSelect = useCallback((node: Node) => {
    setSelectedNode(node);
  }, []);

  const handleNodeConfigUpdate = useCallback((nodeId: string, config: any) => {
    setWorkflow(prev => ({
      ...prev,
      nodes: prev.nodes.map(node =>
        node.id === nodeId
          ? { ...node, data: { ...node.data, config } }
          : node
      ),
    }));
  }, []);

  return (
    <ReactFlowProvider>
      <Container maxWidth={false} sx={{ mt: 2, mb: 2, height: 'calc(100vh - 100px)' }}>
        <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
          <Box>
            <TextField
              value={workflow.name}
              onChange={(e) => setWorkflow(prev => ({ ...prev, name: e.target.value }))}
              placeholder="Workflow Name"
              variant="outlined"
              size="small"
              sx={{ mr: 2 }}
            />
            <TextField
              value={workflow.description}
              onChange={(e) => setWorkflow(prev => ({ ...prev, description: e.target.value }))}
              placeholder="Description"
              variant="outlined"
              size="small"
              sx={{ width: 300 }}
            />
          </Box>
          <Box>
            <Button
              variant="contained"
              startIcon={<SaveIcon />}
              onClick={handleSave}
              sx={{ mr: 1 }}
            >
              Save
            </Button>
            <Button
              variant="contained"
              startIcon={<RunIcon />}
              color="success"
              onClick={() => {/* Implement run workflow */}}
            >
              Run
            </Button>
          </Box>
        </Box>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        <Box display="flex" height="calc(100vh - 200px)">
          <Drawer
            variant="persistent"
            anchor="left"
            open={isPaletteOpen}
            sx={{
              width: 240,
              flexShrink: 0,
              '& .MuiDrawer-paper': {
                width: 240,
                position: 'relative',
                height: '100%',
              },
            }}
          >
            <NodePalette onDragStart={() => {}} />
          </Drawer>

          <Box flex={1}>
            <WorkflowEditor
              initialNodes={workflow.nodes}
              initialEdges={workflow.edges}
              onNodesChange={handleNodesChange}
              onEdgesChange={handleEdgesChange}
              onNodeSelect={handleNodeSelect}
            />
          </Box>

          {selectedNode && (
            <Drawer
              variant="persistent"
              anchor="right"
              open={!!selectedNode}
              sx={{
                width: 300,
                flexShrink: 0,
                '& .MuiDrawer-paper': {
                  width: 300,
                  position: 'relative',
                  height: '100%',
                },
              }}
            >
              <NodeConfigPanel
                node={selectedNode}
                onClose={() => setSelectedNode(null)}
                onConfigUpdate={handleNodeConfigUpdate}
              />
            </Drawer>
          )}
        </Box>
      </Container>
    </ReactFlowProvider>
  );
};

export default WorkflowEditPage;
