import { Box, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import { Dashboard, AccountTree, PlayArrow } from '@mui/icons-material';
import { Link } from 'react-router-dom';

export const Navigation = () => {
  const menuItems = [
    { text: 'Dashboard', icon: <Dashboard />, path: '/' },
    { text: 'Graphs', icon: <AccountTree />, path: '/graph' },
    { text: 'Executions', icon: <PlayArrow />, path: '/executions' },
  ];

  return (
    <Box sx={{ width: 240 }}>
      <List>
        {menuItems.map((item) => (
          <ListItem
            button
            component={Link}
            to={item.path}
            key={item.text}
          >
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.text} />
          </ListItem>
        ))}
      </List>
    </Box>
  );
};
