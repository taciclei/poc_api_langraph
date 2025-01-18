import React, { memo } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, Box } from '@mui/material';

const CustomNode = ({ data }: NodeProps) => {
  return (
    <Paper
      sx={{
        padding: 2,
        minWidth: 180,
        borderRadius: 2,
        background: 'linear-gradient(45deg, #1a237e 30%, #283593 90%)',
        color: 'white',
      }}
    >
      <Handle type="target" position={Position.Left} />
      <Box>
        <Typography variant="subtitle1">{data.label}</Typography>
        <Typography variant="caption">{data.type}</Typography>
      </Box>
      <Handle type="source" position={Position.Right} />
    </Paper>
  );
};

export default memo(CustomNode);
