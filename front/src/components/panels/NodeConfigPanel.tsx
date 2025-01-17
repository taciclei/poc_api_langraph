import { useCallback } from 'react';
import {
  Drawer,
  Box,
  Typography,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Button,
  IconButton,
  Divider,
} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import { LangGraphNode } from '../../types/graph';

interface NodeConfigPanelProps {
  node: LangGraphNode | null;
  open: boolean;
  onClose: () => void;
  onUpdate: (nodeId: string, updates: Partial<LangGraphNode>) => void;
}

const NodeConfigPanel = ({ node, open, onClose, onUpdate }: NodeConfigPanelProps) => {
  const handleLabelChange = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      if (node) {
        onUpdate(node.id, {
          data: { ...node.data, label: event.target.value },
        });
      }
    },
    [node, onUpdate]
  );

  const getConfigFields = useCallback(() => {
    if (!node) return null;

    switch (node.data.type) {
      case 'llm':
        return (
          <>
            <FormControl fullWidth margin="normal">
              <InputLabel>Model</InputLabel>
              <Select
                value={node.data.config.model || ''}
                onChange={(e) =>
                  onUpdate(node.id, {
                    data: {
                      ...node.data,
                      config: { ...node.data.config, model: e.target.value },
                    },
                  })
                }
              >
                <MenuItem value="gpt-4">GPT-4</MenuItem>
                <MenuItem value="gpt-3.5-turbo">GPT-3.5 Turbo</MenuItem>
                <MenuItem value="claude-2">Claude 2</MenuItem>
              </Select>
            </FormControl>
            <TextField
              fullWidth
              margin="normal"
              label="Temperature"
              type="number"
              inputProps={{ min: 0, max: 1, step: 0.1 }}
              value={node.data.config.temperature || 0.7}
              onChange={(e) =>
                onUpdate(node.id, {
                  data: {
                    ...node.data,
                    config: { ...node.data.config, temperature: parseFloat(e.target.value) },
                  },
                })
              }
            />
          </>
        );

      case 'prompt':
        return (
          <TextField
            fullWidth
            margin="normal"
            label="Template"
            multiline
            rows={4}
            value={node.data.config.template || ''}
            onChange={(e) =>
              onUpdate(node.id, {
                data: {
                  ...node.data,
                  config: { ...node.data.config, template: e.target.value },
                },
              })
            }
          />
        );

      case 'tool':
        return (
          <>
            <FormControl fullWidth margin="normal">
              <InputLabel>Tool Type</InputLabel>
              <Select
                value={node.data.config.toolType || ''}
                onChange={(e) =>
                  onUpdate(node.id, {
                    data: {
                      ...node.data,
                      config: { ...node.data.config, toolType: e.target.value },
                    },
                  })
                }
              >
                <MenuItem value="web-search">Web Search</MenuItem>
                <MenuItem value="calculator">Calculator</MenuItem>
                <MenuItem value="custom">Custom Function</MenuItem>
              </Select>
            </FormControl>
            {node.data.config.toolType === 'custom' && (
              <TextField
                fullWidth
                margin="normal"
                label="Function Code"
                multiline
                rows={4}
                value={node.data.config.functionCode || ''}
                onChange={(e) =>
                  onUpdate(node.id, {
                    data: {
                      ...node.data,
                      config: { ...node.data.config, functionCode: e.target.value },
                    },
                  })
                }
              />
            )}
          </>
        );

      default:
        return null;
    }
  }, [node, onUpdate]);

  if (!node) return null;

  return (
    <Drawer
      anchor="right"
      open={open}
      onClose={onClose}
      PaperProps={{
        sx: { width: 340 },
      }}
    >
      <Box sx={{ p: 2 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
          <Typography variant="h6">Node Configuration</Typography>
          <IconButton onClick={onClose}>
            <CloseIcon />
          </IconButton>
        </Box>
        <Divider sx={{ mb: 2 }} />
        
        <TextField
          fullWidth
          label="Label"
          value={node.data.label}
          onChange={handleLabelChange}
          margin="normal"
        />
        
        <Typography variant="subtitle2" sx={{ mt: 2, mb: 1 }}>
          Type: {node.data.type.toUpperCase()}
        </Typography>
        
        {getConfigFields()}
        
        <Box sx={{ mt: 3 }}>
          <Button
            fullWidth
            variant="contained"
            color="primary"
            onClick={onClose}
          >
            Apply Changes
          </Button>
        </Box>
      </Box>
    </Drawer>
  );
};

export default NodeConfigPanel;
