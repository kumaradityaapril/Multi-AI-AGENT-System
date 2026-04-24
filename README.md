# Multi-AI Agent System

A collaborative multi-agent system built with **LangGraph** and **LangChain** that helps users plan and organize their study goals. The system uses a sequence of specialized AI agents to transform a high-level goal into a detailed, reviewed 10-day study schedule.

## 🚀 Features

- **Planner Agent**: Analyzes the user's goal and creates a high-level summary.
- **Research Agent**: Breaks down the plan into specific study topics.
- **Scheduler Agent**: Generates a structured 10-day study plan based on the topics.
- **Reviewer Agent**: Critiques and optimizes the schedule for better learning outcomes.

## 🛠️ Technology Stack

- **Python**: Core logic.
- **LangGraph**: Orchestrates the agent workflow and state management.
- **LangChain**: Interface for the Large Language Model (LLM).
- **Groq (Llama-3.1-8b)**: High-performance inference for the agents.

## 📋 Prerequisites

- Python 3.8+
- A Groq API Key (get one at [console.groq.com](https://console.groq.com/))

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kumaradityaapril/Multi-AI-AGENT-System.git
   cd Multi-AI-AGENT-System
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install langchain-groq langgraph python-dotenv
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory and add your API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🏃 Usage

Run the main script to start the multi-agent workflow:

```bash
python multi_agent_system.py
```

Follow the prompt to enter your study goal (e.g., "I want to learn Machine Learning in 10 days").

## 🧠 Workflow Architecture

The system follows a linear graph architecture:
`Planner` ➔ `Research` ➔ `Scheduler` ➔ `Reviewer`

Each agent receives the state from the previous one, performs its specialized task, and updates the state for the next agent in the sequence.
