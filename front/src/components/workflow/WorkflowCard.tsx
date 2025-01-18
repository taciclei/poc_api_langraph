import React from 'react';
import {
  Card,
  CardContent,
  CardActions,
  Typography,
  IconButton,
  Box,
  Tooltip,
  CardHeader,
  Avatar,
} from '@mui/material';
import {
  Edit as EditIcon,
  Delete as DeleteIcon,
  PlayArrow as RunIcon,
  AccountTree as WorkflowIcon,
} from '@mui/icons-material';
import { formatDistanceToNow } from 'date-fns';
import { Workflow } from '../../types/workflow';

interface WorkflowCardProps {
  workflow: Workflow;
  onEdit: () => void;
  onDelete: () => void;
  onRun: () => void;
}

const WorkflowCard: React.FC<WorkflowCardProps> = ({
  workflow,
  onEdit,
  onDelete,
  onRun,
}) => {
  return (
    <Card
      sx={{
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        transition: 'transform 0.2s',
        '&:hover': {
          transform: 'translateY(-4px)',
          boxShadow: 4,
        },
      }}
    >
      <CardHeader
        avatar={
          <Avatar sx={{ bgcolor: 'primary.main' }}>
            <WorkflowIcon />
          </Avatar>
        }
        title={workflow.name}
        subheader={`Created ${formatDistanceToNow(new Date(workflow.created_at))} ago`}
      />
      <CardContent sx={{ flexGrow: 1 }}>
        <Typography variant="body2" color="text.secondary">
          {workflow.description || 'No description provided'}
        </Typography>
        <Box sx={{ mt: 2 }}>
          <Typography variant="caption" color="text.secondary">
            {workflow.nodes.length} nodes • {workflow.edges.length} connections
          </Typography>
        </Box>
      </CardContent>
      <CardActions disableSpacing>
        <Box sx={{ ml: 'auto' }}>
          <Tooltip title="Run Workflow">
            <IconButton onClick={onRun} color="primary">
              <RunIcon />
            </IconButton>
          </Tooltip>
          <Tooltip title="Edit">
            <IconButton onClick={onEdit} color="info">
              <EditIcon />
            </IconButton>
          </Tooltip>
          <Tooltip title="Delete">
            <IconButton onClick={onDelete} color="error">
              <DeleteIcon />
            </IconButton>
          </Tooltip>
        </Box>
      </CardActions>
    </Card>
  );
};

export default WorkflowCard;
