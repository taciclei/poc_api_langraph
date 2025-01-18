import React, { useEffect } from 'react';
import {
  Box,
  Button,
  Container,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography
} from '@mui/material';
import { Add as AddIcon } from '@mui/icons-material';
import { useWorkflow } from '../hooks/useWorkflow';
import { useNavigate } from 'react-router-dom';

export const WorkflowListPage: React.FC = () => {
  const { workflows, loading, error, fetchWorkflows } = useWorkflow();
  const navigate = useNavigate();

  useEffect(() => {
    fetchWorkflows();
  }, [fetchWorkflows]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <Container>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Typography variant="h4">Workflows</Typography>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => navigate('/workflows/new')}
        >
          New Workflow
        </Button>
      </Box>

      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Description</TableCell>
              <TableCell>Created At</TableCell>
              <TableCell>Updated At</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {workflows.map((workflow) => (
              <TableRow key={workflow.id}>
                <TableCell>{workflow.name}</TableCell>
                <TableCell>{workflow.description}</TableCell>
                <TableCell>{new Date(workflow.created_at!).toLocaleDateString()}</TableCell>
                <TableCell>{new Date(workflow.updated_at!).toLocaleDateString()}</TableCell>
                <TableCell>
                  <Button
                    variant="outlined"
                    size="small"
                    onClick={() => navigate(`/workflows/${workflow.id}`)}
                  >
                    View
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
};
