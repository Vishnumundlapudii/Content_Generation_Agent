# 🧠 Content Generation Agent

This repository contains an AI-powered content generation application with a backend built using **FastAPI (Uvicorn)**, a frontend built with **Streamlit**, and a **Jupyter Notebook** to demonstrate and debug the agent execution logic.

## 📁 Repository Structure

├── app/ # FastAPI backend ├── ui/ # Streamlit frontend ├── notebooks/ # Jupyter notebooks for debugging ├── requirements.txt └── README.md


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vishnumundlapudii/Content_Generation_Agent.git
cd Content_Generation_Agent
2. Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
⚙️ How to Run
🔹 Option 1: Run Backend with Uvicorn
This starts the FastAPI backend server.

bash
Copy
Edit
uvicorn app.main:app --reload
Visit http://127.0.0.1:8000/docs for the interactive Swagger UI.

The --reload flag enables hot-reloading during development.

Ideal for debugging API routes and backend logic.

🔹 Option 2: Run Frontend with Streamlit
This launches the Streamlit-based user interface.

bash
Copy
Edit
streamlit run ui/app.py
Provides an interactive frontend for using the content generation agent.

Connects to the FastAPI backend for agent execution.

🧪 Agent Debugging & Exploration
To understand how the agents are working internally:

Launch Jupyter:

bash
Copy
Edit
jupyter notebook
Navigate to notebooks/agent_flow_debug.ipynb (or the relevant notebook in the notebooks/ folder).

Explore the logic, steps, and outputs of the agent.

✅ Best Practices
You can run both Uvicorn and Streamlit at the same time for a complete experience.

Use the Jupyter notebook to debug, trace, and understand how the agent works under the hood.

Modular architecture makes it easy to scale or extend.

💡 Future Additions (Suggestions)
Add .env support for config and secrets

Add test cases for APIs and agent steps

Dockerize for container-based deployment

Add multi-agent orchestration (LangGraph or CrewAI)

🧑‍💻 Author
Vishnu Kumar Reddy
