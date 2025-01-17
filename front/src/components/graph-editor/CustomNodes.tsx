import React, { memo } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, Box } from '@mui/material';
import {
  Psychology as LLMIcon,
  TextFields as PromptIcon,
  Code as FunctionIcon,
  Input as InputIcon,
  Output as OutputIcon,
} from '@mui/icons-material';

const nodeTypes = {
  llm: LLMIcon,
  prompt: PromptIcon,
  function: FunctionIcon,
  input: InputIcon,
  output: OutputIcon,
};

const BaseNode = memo(({ data, selected }: NodeProps) => {
  const Icon = nodeTypes[data.type] || FunctionIcon;

  return (
    <Paper
      elevation={selected ? 8 : 2}
      sx={{
        p: 1,
        minWidth: 150,
        border: (theme) =>
          selected ? `2px solid ${theme.palette.primary.main}` : 'none',
      }}
    >
      <Handle type="target" position={Position.Top} />
      <Box display="flex" alignItems="center" gap={1}>
        <Icon color="primary" />
        <Typography variant="body2">{data.label}</Typography>
      </Box>
      <Handle type="source" position={Position.Bottom} />
    </Paper>
  );
});

export const CustomNodes = {
  default: BaseNode,
};
