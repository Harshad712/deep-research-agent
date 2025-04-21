import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

# Initialize Tavily client
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Function to perform web research
def search_web(query):
    response = tavily.search(query)  
    compiled = []

    for item in response:
        # Add check
        if isinstance(item, dict) and "title" in item:
            compiled.append(f"Title: {item['title']}\nURL: {item['url']}\nContent: {item.get('content', 'No content')}\n")
        else:
            compiled.append(str(item))  # Fallback for strings or unexpected structure

    return "\n\n".join(compiled)

