import React, { memo } from 'react'
import { Handle, Position, NodeProps } from 'reactflow'
import { Paper, Typography } from '@mui/material'
import { NodeData } from '../../types/graph'

const CustomNode = memo(({ data }: NodeProps<NodeData>) => {
  return (
    <Paper
      elevation={3}
      sx={{
        padding: 1,
        minWidth: 150,
        backgroundColor: data.color || '#fff',
      }}
    >
      <Handle type="target" position={Position.Left} />
      <Typography variant="subtitle2">{data.type}</Typography>
      <Typography variant="body2">{data.label}</Typography>
      <Handle type="source" position={Position.Right} />
    </Paper>
  )
})

CustomNode.displayName = 'CustomNode'

export default CustomNode
