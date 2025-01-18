import React from 'react'
import { Node } from 'reactflow'
import {
  TextField,
  Switch,
  FormControlLabel,
  Box,
  Typography
} from '@mui/material'
import { NodeData } from '../../types/graph'

interface NodeConfigPanelProps {
  node: Node<NodeData>
  onUpdate: (config: any) => void
}

const NodeConfigPanel: React.FC<NodeConfigPanelProps> = ({ node, onUpdate }) => {
  const handleConfigChange = (field: string, value: any) => {
    const newConfig = {
      ...node.data.config,
      [field]: value
    }
    onUpdate(newConfig)
  }

  return (
    <Box>
      <TextField
        fullWidth
        label="Label"
        value={node.data.label}
        onChange={(e) => handleConfigChange('label', e.target.value)}
        margin="normal"
      />
      {node.data.config && Object.entries(node.data.config).map(([key, value]) => {
        if (typeof value === 'boolean') {
          return (
            <FormControlLabel
              key={key}
              control={
                <Switch
                  checked={value}
                  onChange={(e) => handleConfigChange(key, e.target.checked)}
                />
              }
              label={key}
            />
          )
        }
        return (
          <TextField
            key={key}
            fullWidth
            label={key}
            value={value}
            onChange={(e) => handleConfigChange(key, e.target.value)}
            margin="normal"
          />
        )
      })}
    </Box>
  )
}

export default NodeConfigPanel
