from typing import Dict, Any
from bs4 import BeautifulSoup
import requests
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage

class RetrieverAgent:
    def __init__(self, llm):
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="You are a research agent that extracts relevant information from URLs."),
            ("human", "URL: {url}\nTopic: {topic}\nContent: {content}\nPlease extract relevant information about this topic.")
        ])
        
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        # Fetch content from URL
        print("Retriving Started")
        response = requests.get(state["url"])
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()
        
        # Use LLM to extract relevant information
        messages = self.prompt.format_messages(
            url=state["url"],
            topic=state["topic"],
            content=text_content
        )
        response = await self.llm.ainvoke(messages)
        print("Retriving Completed")
        
        return {
            "research_data": response.content,
            "url": state["url"],
            "topic": state["topic"]
        }