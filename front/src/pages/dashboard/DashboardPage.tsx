import { useEffect } from 'react';
import { Box, Typography, Grid, Paper } from '@mui/material';
import { useGraph } from '../../hooks/useGraph';

const DashboardPage = () => {
  const { graphs, loading, error, fetchGraphs } = useGraph();

  useEffect(() => {
    fetchGraphs();
  }, [fetchGraphs]);

  if (loading) return <Typography>Loading...</Typography>;
  if (error) return <Typography color="error">{error}</Typography>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Recent Graphs
            </Typography>
            {graphs.length === 0 ? (
              <Typography>No graphs found</Typography>
            ) : (
              graphs.map((graph) => (
                <Box key={graph.id} sx={{ mb: 1 }}>
                  <Typography>{graph.name}</Typography>
                </Box>
              ))
            )}
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default DashboardPage;
