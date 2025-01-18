import api from './api';
import { Workflow, WorkflowExecution } from '../types/workflow';

export const workflowService = {
  createWorkflow: async (data: Partial<Workflow>) => {
    const response = await api.post('/workflow/workflows', data);
    return response.data;
  },

  getWorkflow: async (id: string) => {
    const response = await api.get(`/workflow/workflows/${id}`);
    return response.data;
  },

  updateWorkflow: async (id: string, data: Partial<Workflow>) => {
    const response = await api.post('/workflow/workflows/import', {
      ...data,
      id,
      updated_at: new Date().toISOString()
    });
    return response.data;
  },

  listWorkflows: async () => {
    const response = await api.get('/workflow/workflows');
    return response.data;
  },

  deleteWorkflow: async (id: string) => {
    const response = await api.delete(`/workflow/workflows/${id}`);
    return response.data;
  },

  executeWorkflow: async (id: string, input?: Record<string, any>) => {
    const response = await api.post(`/workflow/workflows/${id}/execute`, input);
    return response.data;
  },

  getExecution: async (id: string) => {
    const response = await api.get(`/workflow/executions/${id}`);
    return response.data;
  },

  listExecutions: async (workflowId?: string) => {
    const url = workflowId 
      ? `/workflow/workflows/${workflowId}/executions`
      : '/workflow/executions';
    const response = await api.get(url);
    return response.data;
  }
};
