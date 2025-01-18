import axios from 'axios';
import { GraphData } from '../types/graph';

export const api = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    console.log('Response error:', error);
    return Promise.reject(error);
  }
);

const apiService = {
  // Graph (anciennement Workflow)
  async listWorkflows() {
    return api.get('/graph/graphs');
  },

  async getWorkflow(id: string) {
    return api.get(`/graph/graphs/${id}`);
  },

  async createWorkflow(data: any) {
    return api.post('/graph/graphs', data);
  },

  async updateWorkflow(id: string, data: any) {
    return api.put(`/graph/graphs/${id}`, data);
  },

  async deleteWorkflow(id: string) {
    return api.delete(`/graph/graphs/${id}`);
  },

  // Graph specific
  async getGraph(workflowId: string) {
    return api.get<GraphData>(`/graph/graphs/${workflowId}`);
  },

  async updateGraph(workflowId: string, data: GraphData) {
    return api.put(`/graph/graphs/${workflowId}`, data);
  },

  async executeGraph(workflowId: string) {
    return api.post(`/execution/${workflowId}`, {});
  },

  // Node
  async getNodeTypes() {
    return api.get('/node-types');
  },
};

export default apiService;
