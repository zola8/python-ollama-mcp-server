import asyncio

from fastmcp import Client

# client = Client("http://localhost:8000/mcp")
client = Client("https://excessive-ivory-bobolink.fastmcp.app/mcp")

async def list_tools():
    async with client:
        result = await client.list_tools()
        for tool_item in result:
            print(f"name: {tool_item.name}, description: {tool_item.description}")
            # print(tool_item)


async def call_tool(text: str):
    async with client:
        result = await client.call_tool("tell_joke", {"topic": text})
        print(result.content[-1].text)


if __name__ == "__main__":
    # asyncio.run(list_tools())
    asyncio.run(call_tool("flower"))
