from fastapi import FastAPI

from .tools.config import model
from .tools.get_date_time import get_date_time
from .tools.internet_search import internet_search
from .utils import build_agent

app = FastAPI()

tools = [get_date_time, internet_search]

agent_executor = build_agent(model, tools)


@app.get("/")
async def get_olympick_info():
    prompt = "Determine the current time and date. Identify the most anticipated Olympic event scheduled to occur within the next 24 hours of that time, considering factors such as popularity of the sport, athlete profiles, and historical viewership data. Give the exact time it will start and provide details on how to view. Ensure your final result is accurate and concise"
    response = agent_executor.invoke({"input": prompt})
    return response["output"]
