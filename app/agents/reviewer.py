from typing import Dict, Any
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage

class ReviewerAgent:
    def __init__(self, llm):
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="You are a content reviewer that ensures quality, accuracy, and clarity."),
            ("human", "Content: {content}\nTopic: {topic}\nReview and suggest improvements.")
        ])
    
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        messages = self.prompt.format_messages(
            content=state["draft_content"],
            topic=state["topic"]
        )
        print("Reviewer started")
        response = await self.llm.ainvoke(messages)
        
        # Split the response into content and comments
        parts = response.content.split("---REVIEW COMMENTS---")
        reviewed_content = parts[0].strip()
        review_comments = parts[1].strip() if len(parts) > 1 else "No specific comments."
        
        print("Reviewer completed")
        return {
            "reviewed_content": reviewed_content,
            "review_comments": review_comments
        } 