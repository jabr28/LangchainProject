from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily= TavilyClient() 

@tool
def search(query: str) -> str:
    """
    Tool that search over internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print (f"Searching for: {query}")
    return tavily.search(query=query, num_results=3)    


llm = ChatOpenAI(model="gpt-4o-mini")
tools=[search]
agent=create_agent(model=llm, tools=tools)

def main():
    print("Hello from reactshearchagent!")
    result=agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})
    print(result)

if __name__ == "__main__":
    main()
