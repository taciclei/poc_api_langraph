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
  AccountTree as GraphIcon,
} from '@mui/icons-material';
import { formatDistanceToNow } from 'date-fns';

interface GraphCardProps {
  id: string;
  name: string;
  description: string;
  created_at: string;
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
  onRun: (id: string) => void;
}

const GraphCard: React.FC<GraphCardProps> = ({
  id,
  name,
  description,
  created_at,
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
            <GraphIcon />
          </Avatar>
        }
        title={name}
        subheader={`Created ${formatDistanceToNow(new Date(created_at))} ago`}
      />
      <CardContent sx={{ flexGrow: 1 }}>
        <Typography variant="body2" color="text.secondary">
          {description || 'No description provided'}
        </Typography>
      </CardContent>
      <CardActions disableSpacing>
        <Box sx={{ ml: 'auto' }}>
          <Tooltip title="Run">
            <IconButton onClick={() => onRun(id)} color="primary">
              <RunIcon />
            </IconButton>
          </Tooltip>
          <Tooltip title="Edit">
            <IconButton onClick={() => onEdit(id)} color="info">
              <EditIcon />
            </IconButton>
          </Tooltip>
          <Tooltip title="Delete">
            <IconButton onClick={() => onDelete(id)} color="error">
              <DeleteIcon />
            </IconButton>
          </Tooltip>
        </Box>
      </CardActions>
    </Card>
  );
};

export default GraphCard;
