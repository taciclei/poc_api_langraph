import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Container,
  Grid,
  Button,
  Typography,
  Box,
  CircularProgress,
  Alert,
} from '@mui/material';
import { Add as AddIcon } from '@mui/icons-material';
import { useGraph } from '../../hooks/useGraph';
import GraphCard from '../../components/graph/GraphCard';

const GraphListPage: React.FC = () => {
  const navigate = useNavigate();
  const { graphs, loading, error, fetchGraphs, deleteGraph } = useGraph();

  useEffect(() => {
    fetchGraphs();
  }, [fetchGraphs]);

  const handleCreateGraph = () => {
    navigate('/graphs/new');
  };

  const handleEditGraph = (id: string) => {
    navigate(`/graphs/${id}`);
  };

  const handleDeleteGraph = async (id: string) => {
    if (window.confirm('Are you sure you want to delete this graph?')) {
      await deleteGraph(id);
      fetchGraphs();
    }
  };

  const handleRunGraph = (id: string) => {
    navigate(`/executions/new?graphId=${id}`);
  };

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="60vh">
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Container maxWidth="lg" sx={{ mt: 4 }}>
        <Alert severity="error">{error}</Alert>
      </Container>
    );
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={4}>
        <Typography variant="h4" component="h1" gutterBottom>
          My Graphs
        </Typography>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={handleCreateGraph}
          sx={{
            background: 'linear-gradient(45deg, #2196F3 30%, #21CBF3 90%)',
            boxShadow: '0 3px 5px 2px rgba(33, 203, 243, .3)',
          }}
        >
          Create New Graph
        </Button>
      </Box>
      
      <Grid container spacing={3}>
        {graphs.map((graph) => (
          <Grid item xs={12} sm={6} md={4} key={graph.id}>
            <GraphCard
              {...graph}
              onEdit={handleEditGraph}
              onDelete={handleDeleteGraph}
              onRun={handleRunGraph}
            />
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default GraphListPage;
