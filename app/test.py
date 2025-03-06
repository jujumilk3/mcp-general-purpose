from mcp import ClientSession, StdioServerParameters, stdio_client

params = StdioServerParameters(
    command="./sample_stdio_simplified.py",
    args=["--option", "value"]
)


async def arun():
    async with stdio_client(params) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()


if __name__ == "__main__":
    import anyio
    anyio.run(arun)
