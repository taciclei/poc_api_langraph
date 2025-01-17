import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { DashboardLayout } from './components/layout/DashboardLayout';
import DashboardPage from './pages/dashboard/DashboardPage';
import { GraphEditor } from './pages/graphs/GraphEditor';
import { darkTheme } from './themes/darkTheme';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={darkTheme}>
        <Router>
          <DashboardLayout>
            <Routes>
              <Route path="/" element={<DashboardPage />} />
              <Route path="/graphs" element={<GraphEditor />} />
            </Routes>
          </DashboardLayout>
        </Router>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
