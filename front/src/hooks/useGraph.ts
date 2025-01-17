import { useState, useCallback } from 'react';
import { Graph } from '../types';
import { graphService } from '../services/api';

export const useGraph = () => {
  const [graphs, setGraphs] = useState<Graph[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchGraphs = useCallback(async () => {
    try {
      setLoading(true);
      const data = await graphService.listGraphs();
      setGraphs(data);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  }, []);

  const createGraph = useCallback(async (graphData: Partial<Graph>) => {
    try {
      setLoading(true);
      const newGraph = await graphService.createGraph(graphData);
      setGraphs(prev => [...prev, newGraph]);
      setError(null);
      return newGraph;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  return {
    graphs,
    loading,
    error,
    fetchGraphs,
    createGraph,
  };
};
