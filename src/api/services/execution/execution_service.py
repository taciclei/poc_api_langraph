from typing import Dict, Any, List
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langgraph.graph import Graph
import uuid
from tinydb import TinyDB, Query
from .components.nodes import LLMNode, ProcessingNode, create_tool_node

class ExecutionService:
    def __init__(self):
        self.db = TinyDB('executions.json')
        self.executions = self.db.table('executions')
        self.graphs_db = TinyDB('graphs.json')
        self.graphs = self.graphs_db.table('graphs')
        self.llm = ChatOpenAI()

    def _build_graph(self, graph_config: Dict[str, Any]) -> Graph:
        nodes = {}
        for node in graph_config['nodes']:
            if node['type'] == 'llm':
                nodes[node['id']] = LLMNode(node['config']['prompt_template'])
            elif node['type'] == 'processing':
                # Example of a simple processing node
                nodes[node['id']] = ProcessingNode(
                    lambda x: x['input'].upper() if 'input' in x else x
                )
            elif node['type'] == 'tool':
                tool = Tool(
                    name=node['config']['name'],
                    func=lambda x: x,  # Placeholder for actual tool function
                    description=node['config']['description']
                )
                nodes[node['id']] = create_tool_node(tool)

        workflow = Graph()

        # Add nodes to the graph
        for node_id, node in nodes.items():
            workflow.add_node(node_id, node)

        # Add edges
        for edge in graph_config['edges']:
            workflow.add_edge(edge['source'], edge['target'])

        return workflow.compile()

    async def create_execution(self, graph_id: str, input_data: Dict[str, Any]) -> str:
        execution_id = str(uuid.uuid4())
        execution = {
            "id": execution_id,
            "graph_id": graph_id,
            "input_data": input_data,
            "status": "pending",
            "result": None
        }
        self.executions.insert(execution)
        return execution_id

    async def execute_graph(self, graph_id: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        execution_id = await self.create_execution(graph_id, input_data)
        try:
            result = await self._process_graph(graph_id, input_data)
            self._update_execution(execution_id, "completed", result)
            return {"execution_id": execution_id, "status": "completed", "result": result}
        except Exception as e:
            self._update_execution(execution_id, "failed", str(e))
            raise

    async def _process_graph(self, graph_id: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        Graph = Query()
        graph_config = self.graphs_db.search(Graph.id == graph_id)[0]
        
        workflow = self._build_graph(graph_config)
        
        # Execute the graph
        result = await workflow.ainvoke(input_data)
        return result

    def _update_execution(self, execution_id: str, status: str, result: Any):
        Execution = Query()
        self.executions.update(
            {"status": status, "result": result},
            Execution.id == execution_id
        )

    async def get_execution_status(self, execution_id: str) -> Dict[str, Any]:
        Execution = Query()
        result = self.executions.search(Execution.id == execution_id)
        if not result:
            raise ValueError(f"Execution {execution_id} not found")
        return result[0]

    async def list_executions(self, graph_id: str) -> List[Dict[str, Any]]:
        Execution = Query()
        return self.executions.search(Execution.graph_id == graph_id)
