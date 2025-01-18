import React, { useState } from 'react';
import {
  Box,
  Typography,
  IconButton,
  Divider,
  TextField,
  Button,
  Switch,
  FormControlLabel,
} from '@mui/material';
import { Close as CloseIcon } from '@mui/icons-material';
import { Node } from 'reactflow';

interface NodeConfigPanelProps {
  node: Node;
  onClose: () => void;
  onConfigUpdate: (nodeId: string, config: any) => void;
}

const NodeConfigPanel: React.FC<NodeConfigPanelProps> = ({
  node,
  onClose,
  onConfigUpdate,
}) => {
  const [config, setConfig] = useState(node.data.config || {});

  const handleConfigChange = (key: string, value: any) => {
    const newConfig = { ...config, [key]: value };
    setConfig(newConfig);
    onConfigUpdate(node.id, newConfig);
  };

  return (
    <Box p={2}>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
        <Typography variant="h6">Node Configuration</Typography>
        <IconButton onClick={onClose}>
          <CloseIcon />
        </IconButton>
      </Box>
      <Divider sx={{ mb: 2 }} />

      <Box>
        <TextField
          fullWidth
          label="Node Name"
          value={node.data.name || ''}
          onChange={(e) => handleConfigChange('name', e.target.value)}
          margin="normal"
        />

        <TextField
          fullWidth
          label="Description"
          value={node.data.description || ''}
          onChange={(e) => handleConfigChange('description', e.target.value)}
          margin="normal"
          multiline
          rows={2}
        />

        {/* Add specific configuration fields based on node type */}
        {node.type === 'llm' && (
          <>
            <TextField
              fullWidth
              label="Model"
              value={config.model || ''}
              onChange={(e) => handleConfigChange('model', e.target.value)}
              margin="normal"
              select
              SelectProps={{
                native: true,
              }}
            >
              <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
              <option value="gpt-4">GPT-4</option>
            </TextField>

            <TextField
              fullWidth
              label="Temperature"
              type="number"
              value={config.temperature || 0.7}
              onChange={(e) => handleConfigChange('temperature', parseFloat(e.target.value))}
              margin="normal"
              inputProps={{
                min: 0,
                max: 1,
                step: 0.1,
              }}
            />
          </>
        )}

        {/* Add more node-specific configurations here */}
      </Box>
    </Box>
  );
};

export default NodeConfigPanel;
