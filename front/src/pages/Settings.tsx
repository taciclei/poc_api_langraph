import React from 'react';
import { Typography, Box } from '@mui/material';

const Settings: React.FC = () => {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Settings
      </Typography>
      <Typography>
        Application settings will be available here
      </Typography>
    </Box>
  );
};

export default Settings;
