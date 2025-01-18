import React from 'react';
import { Typography, Box } from '@mui/material';

const Dashboard: React.FC = () => {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Typography>
        Welcome to LangGraph Dashboard
      </Typography>
    </Box>
  );
};

export default Dashboard;
