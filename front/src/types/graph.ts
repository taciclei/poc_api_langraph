export interface GraphData {
  id: string;
  name: string;
  description?: string;
  nodes: any[];
  edges: any[];
  created_at?: string;
  updated_at?: string;
}
