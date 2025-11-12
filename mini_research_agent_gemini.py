"""
Minimal AI Agent — "MiniResearchAgent (Gemini Edition)"
-------------------------------------------------------
Uses Google Gemini 1.5 Pro as the reasoning engine.

Features:
- LLM (Gemini) for reasoning
- DuckDuckGo web search tool
- Conversation memory
- Interactive CLI loop

Requirements:
    pip install google-generativeai langchain langchain-google-genai duckduckgo-search chromadb
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain.memory import ConversationBufferMemory

# -----------------------------
# 1. Configuration
# -----------------------------
from dotenv import load_dotenv
load_dotenv()
google_api_key=os.getenv("GEMINI_API_KEY")

# Set your Google Gemini API key (get from https://makersuite.google.com/)
# os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"

# -----------------------------
# 2. Initialize Core Components
# -----------------------------

# Gemini model as the agent's "brain"
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)

# Memory for context awareness
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Web search tool
search_tool = DuckDuckGoSearchRun()

# -----------------------------
# 3. Create the Agent
# -----------------------------
tools = [search_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# -----------------------------
# 4. Agent Interaction Loop
# -----------------------------
print("\n=== 🧠 MiniResearchAgent (Gemini Edition) ===")
print("Ask research or factual questions. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Agent: Goodbye! 👋")
        break

    try:
        response = agent.run(user_input)
        print(f"\nAgent: {response}\n")
    except Exception as e:
        print(f"[Error] {e}")
