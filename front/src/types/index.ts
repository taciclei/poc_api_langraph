export interface Graph {
  id: string;
  name: string;
  description: string;
  nodes: Node[];
  edges: Edge[];
  created_at: string;
  updated_at: string;
}

export interface Node {
  id: string;
  type: string;
  position: Position;
  data: any;
}

export interface Edge {
  id: string;
  source: string;
  target: string;
  type: string;
}

export interface Position {
  x: number;
  y: number;
}

export interface Execution {
  id: string;
  graph_id: string;
  status: string;
  result: any;
  error: string | null;
  created_at: string;
  updated_at: string;
}
