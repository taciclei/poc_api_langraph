import React from 'react';
import {
  Paper,
  Typography,
  Box,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Switch,
  FormControlLabel,
} from '@mui/material';
import { Node } from 'reactflow';

interface PropertiesPanelProps {
  selectedNode: Node | null;
  onNodeUpdate: (nodeId: string, data: any) => void;
}

export const PropertiesPanel: React.FC<PropertiesPanelProps> = ({
  selectedNode,
  onNodeUpdate,
}) => {
  if (!selectedNode) {
    return (
      <Paper
        sx={{
          width: 300,
          height: '100%',
          p: 2,
          borderRadius: 0,
        }}
      >
        <Typography variant="body2" color="text.secondary">
          Select a node to view its properties
        </Typography>
      </Paper>
    );
  }

  const handleChange = (field: string, value: any) => {
    onNodeUpdate(selectedNode.id, {
      ...selectedNode.data,
      [field]: value,
    });
  };

  return (
    <Paper
      sx={{
        width: 300,
        height: '100%',
        p: 2,
        borderRadius: 0,
        overflow: 'auto',
      }}
    >
      <Typography variant="h6" gutterBottom>
        Node Properties
      </Typography>

      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
        <TextField
          label="Label"
          value={selectedNode.data.label || ''}
          onChange={(e) => handleChange('label', e.target.value)}
          size="small"
          fullWidth
        />

        <FormControl size="small" fullWidth>
          <InputLabel>Node Type</InputLabel>
          <Select
            value={selectedNode.data.type || 'default'}
            onChange={(e) => handleChange('type', e.target.value)}
            label="Node Type"
          >
            <MenuItem value="llm">LLM</MenuItem>
            <MenuItem value="prompt">Prompt</MenuItem>
            <MenuItem value="function">Function</MenuItem>
            <MenuItem value="input">Input</MenuItem>
            <MenuItem value="output">Output</MenuItem>
          </Select>
        </FormControl>

        {selectedNode.data.type === 'llm' && (
          <>
            <TextField
              label="Model"
              value={selectedNode.data.config?.model || ''}
              onChange={(e) =>
                handleChange('config', {
                  ...selectedNode.data.config,
                  model: e.target.value,
                })
              }
              size="small"
              fullWidth
            />
            <TextField
              label="Temperature"
              type="number"
              value={selectedNode.data.config?.temperature || 0.7}
              onChange={(e) =>
                handleChange('config', {
                  ...selectedNode.data.config,
                  temperature: parseFloat(e.target.value),
                })
              }
              size="small"
              fullWidth
              inputProps={{ step: 0.1, min: 0, max: 1 }}
            />
          </>
        )}

        {selectedNode.data.type === 'prompt' && (
          <TextField
            label="Template"
            value={selectedNode.data.config?.template || ''}
            onChange={(e) =>
              handleChange('config', {
                ...selectedNode.data.config,
                template: e.target.value,
              })
            }
            size="small"
            fullWidth
            multiline
            rows={4}
          />
        )}

        <FormControlLabel
          control={
            <Switch
              checked={selectedNode.data.enabled ?? true}
              onChange={(e) => handleChange('enabled', e.target.checked)}
            />
          }
          label="Enabled"
        />
      </Box>
    </Paper>
  );
};
