from typing import Dict, Any, TypedDict
from langgraph.graph import Graph, StateGraph
from langchain_openai import ChatOpenAI
from app.agents.retriever import RetrieverAgent
from app.agents.writer import WriterAgent
from app.agents.reviewer import ReviewerAgent
from app.agents.formatter import FormatterAgent
from dotenv import load_dotenv
import os



load_dotenv()

class WorkflowState(TypedDict):
    url: str
    topic: str
    research_data: str | None
    draft_content: str | None
    reviewed_content: str | None
    review_comments: str | None
    formatted_content: str | None

class ContentGenerationWorkflow:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7)
        self.retriever = RetrieverAgent(self.llm)
        self.writer = WriterAgent(self.llm)
        self.reviewer = ReviewerAgent(self.llm)
        self.formatter = FormatterAgent(self.llm)
        
    def build_graph(self):
        workflow = StateGraph(WorkflowState)
        
        # Define the nodes
        workflow.add_node("retriever", self.retriever.process)
        workflow.add_node("writer", self.writer.process)
        workflow.add_node("reviewer", self.reviewer.process)
        workflow.add_node("formatter", self.formatter.process)
        
        # Define the edges with conditional logic
        workflow.add_edge("retriever", "writer")
        workflow.add_edge("writer", "reviewer")
        workflow.add_edge("reviewer", "formatter")
        
        # Set the entry point
        workflow.set_entry_point("retriever")
        
        # Set the exit point
        workflow.set_finish_point("formatter")
        
        return workflow.compile()
    
    async def run(self, url: str, topic: str) -> Dict[str, Any]:
        graph = self.build_graph()
        
        # Initialize the state
        initial_state = WorkflowState(
            url=url,
            topic=topic,
            research_data=None,
            draft_content=None,
            reviewed_content=None,
            review_comments=None,
            formatted_content=None
        )
        
        result = await graph.ainvoke(initial_state)
        return result 