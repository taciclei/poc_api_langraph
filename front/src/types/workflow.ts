import { Node, Edge } from 'reactflow';

export interface Workflow {
  id: string;
  name: string;
  description?: string;
  created_at: string;
  updated_at: string;
  nodes: Node[];
  edges: Edge[];
}

export interface WorkflowInput {
  name: string;
  description?: string;
  nodes: Node[];
  edges: Edge[];
}
