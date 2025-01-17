import { Node, Edge } from 'reactflow';

export interface NodeConfig {
  model?: string;
  template?: string;
  toolType?: string;
  [key: string]: any;
}

export interface NodeData {
  label: string;
  type: 'llm' | 'prompt' | 'tool' | 'output';
  config: NodeConfig;
}

export interface LangGraphNode extends Node {
  data: NodeData;
}

export interface LangGraphEdge extends Edge {}
