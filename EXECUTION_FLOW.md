# Content Generation System - Execution Flow Documentation

## Overview
This document explains the step-by-step execution flow of the content generation system built using LangGraph and FastAPI. The system uses four specialized agents working in sequence to generate, review, and format content.

## Core Components

### 1. State Management
```python
class WorkflowState(TypedDict):
    url: str                    # Input URL to process
    topic: str                  # Topic for content generation
    research_data: str | None   # Data extracted by retriever
    draft_content: str | None   # Content written by writer
    reviewed_content: str | None # Content reviewed by reviewer
    review_comments: str | None  # Review feedback
    formatted_content: str | None # Final MDX formatted content
```
This TypedDict defines the complete state that flows through the system, ensuring type safety and clear data structure.

## Agent Execution Flow

### 1. Retriever Agent
```python
async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
```
**Execution Steps:**
1. Receives initial state with `url` and `topic`
2. Fetches webpage content using requests
3. Parses HTML with BeautifulSoup
4. Processes content through LLM using prompt template
5. Returns state with:
   - Original URL
   - Original topic
   - Extracted research_data

### 2. Writer Agent
```python
async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
```
**Execution Steps:**
1. Receives state with research_data from Retriever
2. Processes research data through LLM using writing prompt
3. Returns state with:
   - Original topic
   - New draft_content

### 3. Reviewer Agent
```python
async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
```
**Execution Steps:**
1. Receives state with draft_content
2. Reviews content through LLM using review prompt
3. Splits response into content and comments
4. Returns state with:
   - reviewed_content
   - review_comments

### 4. Formatter Agent
```python
async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
```
**Execution Steps:**
1. Receives state with reviewed_content
2. Formats content into MDX through LLM
3. Returns state with:
   - formatted_content (final MDX output)

## Workflow Orchestration

### Graph Construction
```python
def build_graph(self):
    workflow = StateGraph(WorkflowState)
```
**Setup Steps:**
1. Creates StateGraph with defined WorkflowState
2. Adds nodes for each agent
3. Defines sequential edges between agents
4. Sets entry point (retriever) and exit point (formatter)

### Workflow Execution
```python
async def run(self, url: str, topic: str) -> Dict[str, Any]:
```
**Steps:**
1. Builds the graph
2. Initializes WorkflowState with input parameters
3. Executes the graph with initial state
4. Returns final state containing formatted content

## State Transitions

1. **Initial State**
   ```python
   {
       "url": "input_url",
       "topic": "input_topic",
       "research_data": None,
       "draft_content": None,
       "reviewed_content": None,
       "review_comments": None,
       "formatted_content": None
   }
   ```

2. **After Retriever**
   ```python
   {
       "url": "input_url",
       "topic": "input_topic",
       "research_data": "extracted_data",
       # Other fields remain None
   }
   ```

3. **After Writer**
   ```python
   {
       "topic": "input_topic",
       "research_data": "extracted_data",
       "draft_content": "written_content",
       # Other fields remain as before
   }
   ```

4. **After Reviewer**
   ```python
   {
       # Previous fields remain
       "reviewed_content": "improved_content",
       "review_comments": "review_feedback"
   }
   ```

5. **Final State**
   ```python
   {
       # All previous fields remain
       "formatted_content": "mdx_formatted_content"
   }
   ```

## Error Handling

Each agent maintains the state consistency by:
1. Accessing only required fields from the input state
2. Adding new fields without modifying unrelated ones
3. Ensuring type safety through TypedDict
4. Maintaining the chain of data through the workflow

## API Integration

The workflow is exposed through FastAPI:
1. Receives URL and topic through POST request
2. Initializes workflow with parameters
3. Returns formatted MDX content
4. Handles errors and provides appropriate responses

## Best Practices

1. Each agent focuses on a single responsibility
2. State is immutable within each agent
3. Clear type definitions for state management
4. Sequential processing with clear data flow
5. Proper error handling at each step

This execution flow ensures:
- Clear separation of concerns
- Type safety throughout the process
- Maintainable and testable code
- Scalable architecture
- Reliable state management 