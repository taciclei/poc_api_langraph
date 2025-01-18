import React from 'react';
import { Link as RouterLink, useLocation } from 'react-router-dom';
import {
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  ListItemButton,
} from '@mui/material';
import {
  Dashboard as DashboardIcon,
  AccountTree as GraphIcon,
  Settings as SettingsIcon,
} from '@mui/icons-material';

const navigationItems = [
  { text: 'Dashboard', icon: <DashboardIcon />, path: '/dashboard' },
  { text: 'Graphs', icon: <GraphIcon />, path: '/graphs' },
  { text: 'Settings', icon: <SettingsIcon />, path: '/settings' },
];

const Navigation: React.FC = () => {
  const location = useLocation();

  return (
    <List>
      {navigationItems.map((item) => (
        <ListItem key={item.text} disablePadding>
          <ListItemButton
            component={RouterLink}
            to={item.path}
            selected={location.pathname === item.path}
          >
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.text} />
          </ListItemButton>
        </ListItem>
      ))}
    </List>
  );
};

export default Navigation;
