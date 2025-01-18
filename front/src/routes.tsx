import { Routes, Route, Navigate } from 'react-router-dom';
import GraphListPage from './pages/graphs/GraphListPage';
import GraphEditPage from './pages/graphs/GraphEditPage';
import WorkflowListPage from './pages/workflows/WorkflowListPage';
import WorkflowEditPage from './pages/workflows/WorkflowEditPage';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/workflows" replace />} />
      <Route path="/graphs" element={<GraphListPage />} />
      <Route path="/graphs/new" element={<GraphEditPage />} />
      <Route path="/graphs/:id" element={<GraphEditPage />} />
      <Route path="/workflows" element={<WorkflowListPage />} />
      <Route path="/workflows/new" element={<WorkflowEditPage />} />
      <Route path="/workflows/:id" element={<WorkflowEditPage />} />
    </Routes>
  );
};

export default AppRoutes;
