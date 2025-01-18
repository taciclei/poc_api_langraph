import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Typography, Box, Button, Grid, Card, CardContent, CardActions } from '@mui/material';
import { Add as AddIcon } from '@mui/icons-material';
import { useGraph } from '../hooks/useGraph';

const GraphList: React.FC = () => {
  const navigate = useNavigate();
  const { graphs, loading, error, fetchGraphs } = useGraph();

  useEffect(() => {
    fetchGraphs();
  }, [fetchGraphs]);

  return (
    <Box>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
        <Typography variant="h4">Graphs</Typography>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => navigate('/graphs/new')}
        >
          New Graph
        </Button>
      </Box>

      {loading && <Typography>Loading...</Typography>}
      {error && <Typography color="error">{error}</Typography>}
      
      <Grid container spacing={3}>
        {graphs.map((graph) => (
          <Grid item xs={12} sm={6} md={4} key={graph.id}>
            <Card>
              <CardContent>
                <Typography variant="h6">{graph.name}</Typography>
                <Typography variant="body2" color="textSecondary">
                  {graph.description}
                </Typography>
              </CardContent>
              <CardActions>
                <Button size="small" onClick={() => navigate(`/graphs/${graph.id}`)}>
                  Open
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default GraphList;
