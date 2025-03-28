from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.workflows.content_workflow import ContentGenerationWorkflow

app = FastAPI(title="Content Generation API")

class ContentRequest(BaseModel):
    url: str
    topic: str

class ContentResponse(BaseModel):
    mdx_content: str
    status: str

@app.post("/generate-content", response_model=ContentResponse)
async def generate_content(request: ContentRequest):
    try:
        workflow = ContentGenerationWorkflow()
        result = await workflow.run(request.url, request.topic)
        
        return ContentResponse(
            mdx_content=result["formatted_content"],
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 