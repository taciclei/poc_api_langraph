import { useState, useCallback } from 'react';
import apiService from '../services/api';

export interface Workflow {
  id: string;
  name: string;
  description?: string;
  created_at?: string;
  updated_at?: string;
}

export const useWorkflow = () => {
  const [workflows, setWorkflows] = useState<Workflow[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchWorkflows = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await apiService.listWorkflows();
      setWorkflows(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  }, []);

  const getWorkflow = useCallback(async (id: string) => {
    try {
      setLoading(true);
      setError(null);
      return await apiService.getWorkflow(id);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const createWorkflow = useCallback(async (data: Partial<Workflow>) => {
    try {
      setLoading(true);
      setError(null);
      const result = await apiService.createWorkflow(data);
      await fetchWorkflows();
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [fetchWorkflows]);

  const updateWorkflow = useCallback(async (id: string, data: Partial<Workflow>) => {
    try {
      setLoading(true);
      setError(null);
      const result = await apiService.updateWorkflow(id, data);
      await fetchWorkflows();
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [fetchWorkflows]);

  const deleteWorkflow = useCallback(async (id: string) => {
    try {
      setLoading(true);
      setError(null);
      await apiService.deleteWorkflow(id);
      await fetchWorkflows();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [fetchWorkflows]);

  return {
    workflows,
    loading,
    error,
    fetchWorkflows,
    getWorkflow,
    createWorkflow,
    updateWorkflow,
    deleteWorkflow
  };
};
