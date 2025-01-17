import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

export const graphService = {
  createGraph: async (data: any) => {
    const response = await api.post('/graph', data);
    return response.data;
  },
  getGraph: async (id: string) => {
    const response = await api.get(`/graph/${id}`);
    return response.data;
  },
  listGraphs: async () => {
    const response = await api.get('/graph');
    return response.data;
  }
};

export const executionService = {
  createExecution: async (data: any) => {
    const response = await api.post('/execution', data);
    return response.data;
  },
  getExecution: async (id: string) => {
    const response = await api.get(`/execution/${id}`);
    return response.data;
  },
  listExecutions: async () => {
    const response = await api.get('/execution');
    return response.data;
  }
};

export default api;
