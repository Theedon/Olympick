from datetime import datetime

from langchain_community.tools import tool


@tool
def get_date_time() -> str:
    """Returns the current date and time"""

    current_date = datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
    return f"current date and time is {current_date}"
