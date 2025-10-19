# MiniResearchAgent (Gemini Edition)

A **minimal end-to-end AI Agent** powered by **Google Gemini 1.5 Pro** and **LangChain**.
This project demonstrates how to build an autonomous AI assistant that can:

- Search the web
- Reason over information
- Remember previous interactions
- Summarize and explain complex topics

It’s designed as a **learning project** — perfect for anyone who wants to **understand AI agents by building one from scratch**.

---

## Features

Uses **Gemini 1.5 Pro** as the reasoning engine
Integrates **DuckDuckGo Search** for real-time information
Maintains **short-term memory** across turns
Built using **LangChain Agents** and **ReAct reasoning**
Fully runnable in a single Python script

---

## Architecture Overview

| Component                  | Role                                                               |
| -------------------------- | ------------------------------------------------------------------ |
| **Gemini (LLM)**           | The agent’s brain – handles reasoning, planning, and summarization |
| **LangChain Agent**        | Orchestrates tools, memory, and the LLM                            |
| **DuckDuckGo Search Tool** | Allows the agent to browse the web                                 |
| **Memory Buffer**          | Keeps conversation context across turns                            |
| **CLI Loop**               | Simple terminal-based interaction                                  |

---

## Installation

### 1. Clone or create the file

Save the script as:

```
mini_research_agent_gemini.py
```

### 2. Install dependencies

```bash
pip install google-generativeai langchain langchain-google-genai duckduckgo-search chromadb
```

### 3. Set up your Gemini API key

Get your **Google Gemini API key** from [https://makersuite.google.com/](https://makersuite.google.com/)

Then set it in your environment:

```bash
export GOOGLE_API_KEY="your_api_key_here"      # macOS/Linux
setx GOOGLE_API_KEY "your_api_key_here"        # Windows
```

Or directly paste it in the Python file.

---

## Running the Agent

```bash
python mini_research_agent_gemini.py
```

Then interact via CLI:

```
You: Find recent advancements in small language models in 2025
Agent: ...
```

---

## Example Prompts

Try questions like:

- “Summarize the latest research on multi-agent systems.”
- “Compare Gemini 1.5 Pro and GPT-4o.”
- “Explain how reinforcement learning with human feedback works.”
- “What are the best open-source AI agent frameworks?”

---

## How It Works

```text
User Query → Gemini (LLM reasoning)
            → Tool selection (e.g., search)
            → Information retrieval
            → Summarized response
            → Memory stored for next turn
```

It follows the **ReAct pattern** (Reasoning + Acting), where the agent:

1. Thinks about what to do
2. Uses tools when needed
3. Reflects on results
4. Produces a final answer

---

## Learn by Extending

After getting this running, try adding:

| Upgrade                  | What You’ll Learn                     |
| ------------------------ | ------------------------------------- |
| Vector Memory (ChromaDB) | Persistent memory & embeddings        |
| Python REPL Tool         | Code execution capabilities           |
| File I/O                 | Read research papers, write summaries |
| Reflection               | Self-evaluation & improvement loops   |
| Streamlit UI             | Interactive web interface             |

---

## Tech Stack

- **Language Model:** Google Gemini 1.5 Pro
- **Framework:** LangChain
- **Tools:** DuckDuckGo Search
- **Memory:** ConversationBufferMemory
- **Language:** Python 3.11+

---

## Project Goals

This project aims to help you:

- Understand how AI agents work (LLM + tools + memory)
- Build your own from the ground up
- Use LangChain and Gemini effectively
- Expand from a minimal agent to a fully autonomous system
