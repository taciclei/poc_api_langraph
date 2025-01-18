import { useState, useCallback } from 'react';
import apiService from '../services/api';
import { GraphData } from '../types/graph';

export const useGraph = () => {
  const [graphs, setGraphs] = useState<GraphData[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchGraphs = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await apiService.listGraphs();
      setGraphs(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  }, []);

  const getGraph = useCallback(async (id: string) => {
    try {
      setLoading(true);
      setError(null);
      return await apiService.getGraph(id);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const createGraph = useCallback(async (data: any) => {
    try {
      setLoading(true);
      setError(null);
      const result = await apiService.createGraph(data);
      await fetchGraphs();
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [fetchGraphs]);

  const updateGraph = useCallback(async (id: string, data: Partial<GraphData>) => {
    try {
      setLoading(true);
      setError(null);
      const result = await apiService.updateGraph(id, data);
      await fetchGraphs();
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [fetchGraphs]);

  const deleteGraph = useCallback(async (id: string) => {
    try {
      setLoading(true);
      setError(null);
      await apiService.deleteGraph(id);
      await fetchGraphs();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [fetchGraphs]);

  return {
    graphs,
    loading,
    error,
    fetchGraphs,
    getGraph,
    createGraph,
    updateGraph,
    deleteGraph
  };
};
