import React from 'react';
import { Grid, Paper, Typography, Box } from '@mui/material';
import { ResponsiveLine } from '@nivo/line';
import { ResponsivePie } from '@nivo/pie';

const DashboardPage: React.FC = () => {
  // Données simulées pour les graphiques
  const lineData = [
    {
      id: 'executions',
      data: [
        { x: '2024-01', y: 24 },
        { x: '2024-02', y: 45 },
        { x: '2024-03', y: 65 },
      ],
    },
  ];

  const pieData = [
    { id: 'success', value: 75, label: 'Success' },
    { id: 'failed', value: 25, label: 'Failed' },
  ];

  return (
    <Grid container spacing={3}>
      <Grid item xs={12}>
        <Typography variant="h4" gutterBottom>
          Dashboard
        </Typography>
      </Grid>
      
      <Grid item xs={12} md={8}>
        <Paper sx={{ p: 2, height: 400 }}>
          <Typography variant="h6" gutterBottom>
            Execution History
          </Typography>
          <Box sx={{ height: 300 }}>
            <ResponsiveLine
              data={lineData}
              margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
              xScale={{ type: 'point' }}
              yScale={{ type: 'linear', min: 'auto', max: 'auto' }}
              axisTop={null}
              axisRight={null}
              pointSize={10}
              pointColor={{ theme: 'background' }}
              pointBorderWidth={2}
              pointBorderColor={{ from: 'serieColor' }}
              enablePointLabel={true}
              pointLabel="y"
              pointLabelYOffset={-12}
            />
          </Box>
        </Paper>
      </Grid>

      <Grid item xs={12} md={4}>
        <Paper sx={{ p: 2, height: 400 }}>
          <Typography variant="h6" gutterBottom>
            Execution Status
          </Typography>
          <Box sx={{ height: 300 }}>
            <ResponsivePie
              data={pieData}
              margin={{ top: 40, right: 80, bottom: 80, left: 80 }}
              innerRadius={0.5}
              padAngle={0.7}
              cornerRadius={3}
              activeOuterRadiusOffset={8}
              colors={{ scheme: 'nivo' }}
              arcLinkLabelsSkipAngle={10}
              arcLinkLabelsTextColor="#333333"
              arcLinkLabelsThickness={2}
              arcLinkLabelsColor={{ from: 'color' }}
              arcLabelsSkipAngle={10}
              arcLabelsTextColor="#ffffff"
            />
          </Box>
        </Paper>
      </Grid>
    </Grid>
  );
};

export default DashboardPage;
