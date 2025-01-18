import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Box, Typography } from '@mui/material';
import { useGraph } from '../hooks/useGraph';
import { GraphData } from '../types/graph';

const GraphEditor: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { getGraph, updateGraph, loading, error } = useGraph();
  const [graph, setGraph] = useState<GraphData | null>(null);

  useEffect(() => {
    if (id && id !== 'new') {
      getGraph(id).then(setGraph);
    }
  }, [id, getGraph]);

  if (loading) return <Typography>Loading...</Typography>;
  if (error) return <Typography color="error">{error}</Typography>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        {graph?.name || 'New Graph'}
      </Typography>
      {/* WorkflowEditor will be implemented later */}
      <Typography>Graph Editor Coming Soon</Typography>
    </Box>
  );
};

export default GraphEditor;
