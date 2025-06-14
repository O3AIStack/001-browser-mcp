import logfire
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

logfire.configure(token='pylf_v1_eu_mzLmz60hCt4gMcsnKJ9Q9L6yC9kzst5Lx3GQstkHd6zf')
logfire.info('Hello, {place}!', place='World')

logfire.configure(scrubbing=False)
logfire.instrument_mcp()
logfire.instrument_pydantic_ai()



# enables browser control (Google Chrome)
browser_mcp = MCPServerStdio(
    'npx',
    args=[
        '-Y',
        '@playwright/mcp@latest',
    ]
)

agent = Agent(
    'anthropic:claude-3-7-sonnet-latest',
    mcp_servers=[browser_mcp],
)

async def main():
    async with agent.run_mcp_servers():
        result = await agent.run(
            'get the most recent blog post from pydantic.dev '
            'which should contain multiple announcements, '
            'summaries thise announcements as a list'
        )
        print(result.data)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())


