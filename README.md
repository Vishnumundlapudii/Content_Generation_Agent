# Content Generation API

This is an intelligent content generation system that uses multiple AI agents to research, write, review, and format content based on a given URL and topic. The system is built using LangGraph for agent orchestration and FastAPI for the API interface.

## Features

- URL content retrieval and analysis
- AI-powered content writing
- Content review and improvement
- MDX formatting
- Multi-agent workflow orchestration

## Prerequisites

- Python 3.9+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/content-generator.git
cd content-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your OpenAI API key: 