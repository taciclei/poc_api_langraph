import { memo } from 'react';
import { Handle, Position } from 'reactflow';
import { Box, Typography, Chip, Tooltip } from '@mui/material';
import { nodeTypeStyles, nodeCommonStyles, handleStyles, chipStyles } from './styles/nodeStyles';

const BaseNode = ({ data, selected }: any) => {
  const typeStyle = nodeTypeStyles[data.type];

  return (
    <Box
      sx={{
        ...nodeCommonStyles,
        backgroundColor: typeStyle.backgroundColor,
        borderColor: selected ? typeStyle.borderColor : 'rgba(255, 255, 255, 0.12)',
        position: 'relative',
        '&::before': {
          content: '""',
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: `radial-gradient(circle at center, ${typeStyle.gradientColor} 0%, transparent 70%)`,
          opacity: selected ? 1 : 0,
          transition: 'opacity 0.2s ease',
          pointerEvents: 'none',
        },
      }}
    >
      <Handle
        type="target"
        position={Position.Top}
        style={{
          ...handleStyles,
          borderColor: typeStyle.borderColor,
          backgroundColor: selected ? typeStyle.borderColor : '#1E1E1E',
        }}
      />
      
      <Box sx={{ p: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 1.5 }}>
          <Typography
            variant="h6"
            component="span"
            sx={{
              mr: 1,
              filter: 'drop-shadow(0 2px 4px rgba(0,0,0,0.2))',
            }}
          >
            {typeStyle.icon}
          </Typography>
          <Typography
            variant="subtitle1"
            fontWeight="600"
            sx={{
              color: selected ? typeStyle.borderColor : 'text.primary',
              transition: 'color 0.2s ease',
            }}
          >
            {data.label}
          </Typography>
        </Box>

        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
          {data.type === 'llm' && data.config.model && (
            <Tooltip title="Model">
              <Chip
                label={data.config.model}
                size="small"
                sx={chipStyles}
              />
            </Tooltip>
          )}
          {data.type === 'prompt' && data.config.template && (
            <Tooltip title="Has Template">
              <Chip
                label="Template"
                size="small"
                sx={chipStyles}
              />
            </Tooltip>
          )}
          {data.type === 'tool' && data.config.toolType && (
            <Tooltip title="Tool Type">
              <Chip
                label={data.config.toolType}
                size="small"
                sx={chipStyles}
              />
            </Tooltip>
          )}
        </Box>

        {selected && (
          <Typography
            variant="caption"
            sx={{
              position: 'absolute',
              bottom: -24,
              left: '50%',
              transform: 'translateX(-50%)',
              backgroundColor: 'rgba(0, 0, 0, 0.8)',
              color: 'rgba(255, 255, 255, 0.7)',
              px: 1,
              py: 0.5,
              borderRadius: 1,
              whiteSpace: 'nowrap',
            }}
          >
            Click to configure
          </Typography>
        )}
      </Box>

      <Handle
        type="source"
        position={Position.Bottom}
        style={{
          ...handleStyles,
          borderColor: typeStyle.borderColor,
          backgroundColor: selected ? typeStyle.borderColor : '#1E1E1E',
        }}
      />
    </Box>
  );
};

export default memo(BaseNode);
