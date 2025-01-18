import { SxProps, Theme } from '@mui/material';

interface NodeTypeStyles {
  backgroundColor: string;
  borderColor: string;
  icon: string;
  gradientColor: string;
}

export const nodeTypeStyles: Record<string, NodeTypeStyles> = {
  llm: {
    backgroundColor: 'rgba(32, 129, 226, 0.12)',
    borderColor: '#2081E2',
    gradientColor: 'rgba(32, 129, 226, 0.05)',
    icon: '🤖',
  },
  prompt: {
    backgroundColor: 'rgba(52, 211, 153, 0.12)',
    borderColor: '#34D399',
    gradientColor: 'rgba(52, 211, 153, 0.05)',
    icon: '📝',
  },
  tool: {
    backgroundColor: 'rgba(251, 191, 36, 0.12)',
    borderColor: '#FBBF24',
    gradientColor: 'rgba(251, 191, 36, 0.05)',
    icon: '🔧',
  },
  output: {
    backgroundColor: 'rgba(167, 139, 250, 0.12)',
    borderColor: '#A78BFA',
    gradientColor: 'rgba(167, 139, 250, 0.05)',
    icon: '📤',
  },
};

export const nodeCommonStyles: SxProps<Theme> = {
  minWidth: 220,
  maxWidth: 320,
  borderRadius: 2,
  border: 2,
  backdropFilter: 'blur(8px)',
  transition: 'all 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
  '&:hover': {
    transform: 'translateY(-2px)',
    boxShadow: '0 8px 16px rgba(0, 0, 0, 0.3)',
  },
};

export const handleStyles = {
  width: 10,
  height: 10,
  borderRadius: '50%',
  border: '2px solid',
  zIndex: 1,
};

export const chipStyles: SxProps<Theme> = {
  height: 24,
  fontSize: '0.75rem',
  backgroundColor: 'rgba(255, 255, 255, 0.08)',
  '&:hover': {
    backgroundColor: 'rgba(255, 255, 255, 0.12)',
  },
};
