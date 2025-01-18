import React from 'react';
import { Box, Paper, Typography, List, ListItem } from '@mui/material';
import {
  Psychology as LLMIcon,
  TextFields as PromptIcon,
  Code as FunctionIcon,
  Input as InputIcon,
  Output as OutputIcon,
} from '@mui/icons-material';

const nodeTypes = [
  { type: 'llm', label: 'LLM Node', icon: LLMIcon, color: '#4CAF50' },
  { type: 'prompt', label: 'Prompt', icon: PromptIcon, color: '#2196F3' },
  { type: 'function', label: 'Function', icon: FunctionIcon, color: '#FF9800' },
  { type: 'input', label: 'Input', icon: InputIcon, color: '#9C27B0' },
  { type: 'output', label: 'Output', icon: OutputIcon, color: '#F44336' },
];

export const NodePalette: React.FC = () => {
  const onDragStart = (event: React.DragEvent, nodeType: string) => {
    event.dataTransfer.setData('application/reactflow', nodeType);
    event.dataTransfer.effectAllowed = 'move';
  };

  return (
    <Paper
      sx={{
        width: 250,
        height: '100%',
        overflow: 'auto',
        borderRadius: 0,
      }}
    >
      <Box sx={{ p: 2 }}>
        <Typography variant="h6" gutterBottom>
          Nodes Palette
        </Typography>
        <List>
          {nodeTypes.map(({ type, label, icon: Icon, color }) => (
            <ListItem
              key={type}
              sx={{
                cursor: 'grab',
                mb: 1,
                '&:hover': {
                  backgroundColor: 'action.hover',
                },
              }}
              draggable
              onDragStart={(e) => onDragStart(e, type)}
            >
              <Paper
                sx={{
                  p: 1,
                  width: '100%',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 1,
                  bgcolor: 'background.paper',
                  border: 1,
                  borderColor: color,
                }}
              >
                <Icon sx={{ color }} />
                <Typography variant="body2">{label}</Typography>
              </Paper>
            </ListItem>
          ))}
        </List>
      </Box>
    </Paper>
  );
};
