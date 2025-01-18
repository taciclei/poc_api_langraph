import React from 'react';
import {
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Typography,
  Box,
  Paper,
} from '@mui/material';
import {
  Chat as ChatIcon,
  Memory as MemoryIcon,
  Storage as StorageIcon,
  Transform as TransformIcon,
} from '@mui/icons-material';

const nodeTypes = [
  {
    type: 'llm',
    name: 'LLM Node',
    description: 'Language Model Processing',
    icon: <ChatIcon />,
  },
  {
    type: 'memory',
    name: 'Memory Node',
    description: 'State Management',
    icon: <MemoryIcon />,
  },
  {
    type: 'storage',
    name: 'Storage Node',
    description: 'Data Storage',
    icon: <StorageIcon />,
  },
  {
    type: 'transform',
    name: 'Transform Node',
    description: 'Data Transformation',
    icon: <TransformIcon />,
  },
];

interface NodePaletteProps {
  onDragStart: (event: React.DragEvent, nodeType: string) => void;
}

const NodePalette: React.FC<NodePaletteProps> = ({ onDragStart }) => {
  return (
    <Box p={2}>
      <Typography variant="h6" gutterBottom>
        Node Types
      </Typography>
      <List>
        {nodeTypes.map((node) => (
          <ListItem
            key={node.type}
            draggable
            onDragStart={(e) => onDragStart(e, node.type)}
            sx={{
              cursor: 'grab',
              '&:hover': {
                bgcolor: 'action.hover',
              },
            }}
          >
            <Paper
              elevation={2}
              sx={{
                p: 2,
                width: '100%',
                background: 'linear-gradient(45deg, #1a237e 30%, #283593 90%)',
              }}
            >
              <Box display="flex" alignItems="center">
                <ListItemIcon sx={{ color: 'white' }}>
                  {node.icon}
                </ListItemIcon>
                <ListItemText
                  primary={
                    <Typography color="white">
                      {node.name}
                    </Typography>
                  }
                  secondary={
                    <Typography variant="body2" color="rgba(255,255,255,0.7)">
                      {node.description}
                    </Typography>
                  }
                />
              </Box>
            </Paper>
          </ListItem>
        ))}
      </List>
    </Box>
  );
};

export default NodePalette;
