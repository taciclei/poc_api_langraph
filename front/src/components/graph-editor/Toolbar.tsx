import React from 'react';
import { Box, IconButton, Tooltip, Divider } from '@mui/material';
import {
  Add as AddIcon,
  Save as SaveIcon,
  PlayArrow as RunIcon,
  Delete as DeleteIcon,
  ZoomIn as ZoomInIcon,
  ZoomOut as ZoomOutIcon,
  CenterFocusStrong as FitViewIcon,
} from '@mui/icons-material';

interface ToolbarProps {
  onSave: () => void;
  onRun: () => void;
  onZoomIn: () => void;
  onZoomOut: () => void;
  onFitView: () => void;
  onDelete: () => void;
}

export const Toolbar: React.FC<ToolbarProps> = ({
  onSave,
  onRun,
  onZoomIn,
  onZoomOut,
  onFitView,
  onDelete,
}) => {
  return (
    <Box
      sx={{
        position: 'absolute',
        top: 20,
        left: '50%',
        transform: 'translateX(-50%)',
        zIndex: 4,
        backgroundColor: 'background.paper',
        borderRadius: 1,
        boxShadow: 3,
        display: 'flex',
        alignItems: 'center',
        padding: 1,
      }}
    >
      <Tooltip title="Save Graph">
        <IconButton onClick={onSave}>
          <SaveIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Run Graph">
        <IconButton onClick={onRun} color="primary">
          <RunIcon />
        </IconButton>
      </Tooltip>
      <Divider orientation="vertical" flexItem sx={{ mx: 1 }} />
      <Tooltip title="Zoom In">
        <IconButton onClick={onZoomIn}>
          <ZoomInIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Zoom Out">
        <IconButton onClick={onZoomOut}>
          <ZoomOutIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Fit View">
        <IconButton onClick={onFitView}>
          <FitViewIcon />
        </IconButton>
      </Tooltip>
      <Divider orientation="vertical" flexItem sx={{ mx: 1 }} />
      <Tooltip title="Delete Selected">
        <IconButton onClick={onDelete} color="error">
          <DeleteIcon />
        </IconButton>
      </Tooltip>
    </Box>
  );
};
