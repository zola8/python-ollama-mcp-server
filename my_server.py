from fastmcp import FastMCP
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

mcp = FastMCP("My MCP Server 🚀")

llm = ChatOllama(model="llama3.2", temperature=0.2)


@mcp.tool(description="Tell a joke about a topic.")
def tell_joke(topic: str) -> str:
    messages = [HumanMessage(f"Generate a funny joke about {topic}")]
    response = llm.invoke(messages)
    return response.content


@mcp.tool(description="Greeting a user.")
def greet(name: str) -> str:
    return f"Hello, {name}!"


# https://gofastmcp.com/getting-started/quickstart

if __name__ == "__main__":
    mcp.run(
        transport="http",
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ]

    )
