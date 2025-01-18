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
import { useWorkflow } from '../../hooks/useWorkflow';
import WorkflowCard from '../../components/workflow/WorkflowCard';

const WorkflowListPage: React.FC = () => {
  const navigate = useNavigate();
  const { workflows, loading, error, fetchWorkflows } = useWorkflow();

  useEffect(() => {
    fetchWorkflows();
  }, [fetchWorkflows]);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="60vh">
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={4}>
        <Typography variant="h4" component="h1" gutterBottom>
          Workflows
        </Typography>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => navigate('/workflows/new')}
          sx={{
            background: 'linear-gradient(45deg, #2196F3 30%, #21CBF3 90%)',
            boxShadow: '0 3px 5px 2px rgba(33, 203, 243, .3)',
          }}
        >
          Create Workflow
        </Button>
      </Box>

      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>
          {error}
        </Alert>
      )}

      <Grid container spacing={3}>
        {workflows.map((workflow) => (
          <Grid item xs={12} sm={6} md={4} key={workflow.id}>
            <WorkflowCard
              workflow={workflow}
              onEdit={() => navigate(`/workflows/${workflow.id}`)}
              onDelete={async () => {
                if (window.confirm('Are you sure you want to delete this workflow?')) {
                  // Implement delete logic
                }
              }}
              onRun={() => navigate(`/workflows/${workflow.id}/run`)}
            />
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default WorkflowListPage;
