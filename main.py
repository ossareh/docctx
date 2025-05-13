from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("docctx")


@mcp.tool()
async def get_docs(name: str) -> str:
    """Get documents for the specified module

    Args:
        name: of the library you want docs for
    """
    return "\n---\n".join(["foo", "bar", name])


if __name__ == "__main__":
    mcp.run(transport="stdio")
