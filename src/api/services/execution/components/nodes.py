from typing import Dict, Any, Annotated
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseMessage
from langgraph.prebuilt import ToolExecutor
from langchain.tools import Tool

class LLMNode:
    def __init__(self, prompt_template: str, llm=None):
        self.llm = llm or ChatOpenAI()
        self.prompt = ChatPromptTemplate.from_template(prompt_template)

    async def __call__(self, state: Dict[str, Any]) -> Dict[str, Any]:
        messages = self.prompt.format_messages(**state)
        response = await self.llm.agenerate([messages])
        return {"result": response.generations[0][0].text}

class ProcessingNode:
    def __init__(self, processor_func):
        self.process = processor_func

    async def __call__(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {"result": self.process(state)}

def create_tool_node(tool: Tool) -> ToolExecutor:
    return ToolExecutor(tools=[tool])
