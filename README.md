
# 🧠 Content Generation Agent

An AI-powered application to generate content using LLM agents.  
Built with **FastAPI** for the backend, **Streamlit** for the frontend, and **Jupyter Notebook** for debugging and experimentation.

---

## 🧰 Tech Stack

- 🔹 FastAPI + Uvicorn (Backend)
- 🔹 Streamlit (Frontend)
- 🔹 Jupyter Notebook (Agent Debugging)
- 🔹 Python 3.8+

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Vishnumundlapudii/Content_Generation_Agent.git
cd Content_Generation_Agent
```

### 2. Create & activate virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🖥️ Option 1: Run backend with FastAPI + Uvicorn

```bash
uvicorn app.main:app --reload
```

- Access docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Ideal for backend debugging and testing APIs

---

### 🌐 Option 2: Run frontend with Streamlit

```bash
streamlit run ui/app.py
```

- Interactive UI connected to backend
- For user-friendly testing and content generation

---

### 🧪 Option 3: Debug or understand agents using Notebook

- Open the notebook ```Building_Agentic_Apllication_Demo.ipynb```
- Useful for experimenting or inspecting agent logic

---

## 📝 Notes

- You can run both `Uvicorn` and `Streamlit` in parallel.
- Notebooks are provided for debugging or walkthroughs.
- Modular architecture makes it easy to plug in new agents or models.

---

## 👨‍💻 Author

**Vishnu Kumar Reddy**  
[GitHub](https://github.com/Vishnumundlapudii) | [LinkedIn](https://www.linkedin.com/in/vishnu-kumar-reddy-512552152/)

---
