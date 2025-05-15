from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("docctx")


@mcp.tool()
async def get_docs(name: str) -> str:
    """Get documents for the specified module

    Args:
        name: of the library you want docs for
    """
    with open(
        "/Users/ossareh/dev/src/github.com/ossareh/docctx/data/python/mcp/doc.md", "r"
    ) as f:
        return f.read()

    return "no files found"


if __name__ == "__main__":
    mcp.run(transport="stdio")
