import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { ThemeProvider, CssBaseline } from '@mui/material';
import { theme } from './theme';
import DashboardLayout from './components/layout/DashboardLayout';
import AppRoutes from './routes';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <DashboardLayout>
          <AppRoutes />
        </DashboardLayout>
      </ThemeProvider>
    </BrowserRouter>
  );
};

export default App;
