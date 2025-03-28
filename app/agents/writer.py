from typing import Dict, Any
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

class WriterAgent:
    def __init__(self, llm):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7, max_tokens=250)
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="You are a content writer that creates well-structured articles based on research data."),
            ("human", "Research Data: {research_data}\nTopic: {topic}\nWrite a comprehensive article.")
        ])
    
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        print("Writing started")
        messages = self.prompt.format_messages(
            research_data=state["research_data"],
            topic=state["topic"]
        )
        response = await self.llm.ainvoke(messages)
        print("Writing Completed")
        
        return {
            "draft_content": response.content,
            "topic": state["topic"]
        } 