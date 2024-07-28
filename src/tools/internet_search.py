from langchain_community.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults


@tool
def internet_search(question: str) -> str:
    """Performs an internet search using the TavilySearchResults tool and returns the search results."""

    search_tool = TavilySearchResults()
    result = search_tool.invoke(question)
    return result
