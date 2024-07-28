# Olympick

Olympick is a backend application using FastAPI and Langchain to determine the most interesting Olympic event of the day. It leverages a Large Language Model (LLM) and integrates tools to fetch real-time data and make informed decisions.

## Technology Stack

- FastAPI: Backend framework
- Langchain: Framework for building agents
- Groq API: API for accessing the LLM
- LLaMA 3.1 70B Versatile: Large language model used for decision-making

## Setup

1. Clone the repository:

   `git clone https://github.com/theedon/olympick.git`

   `cd olympick`

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -U dotenv fastapi uvicorn langchain langchain-groq langchainhub langchain-community
   ```

## Tools

### Get Current Date

Retrieves the current date and time.

### Internet Search

Performs an internet search using Tavily.

## Agent

Creates an agent with the tools.

## Running the Application

Start the application with Uvicorn:

```bash
uvicorn src.main:app --reload
```
