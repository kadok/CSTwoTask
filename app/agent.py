from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
from app.config import Config
from app.data.database import SessionLocal
from app.data.models import Car

def create_agent():
    """
        Cria agente MCP para consultas LLM + DB.
    """
    if not Config.DB_LINK:
        raise ValueError("DB_LINK não definido no .env")

    config = {
        "mcpServers": {
            "postgres": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-postgres",
                    Config.DB_LINK
                ]
            }
        }
    }

    client = MCPClient.from_dict(config)
    llm = ChatOpenAI(model=Config.OPENAI_MODEL)
    return MCPAgent(llm=llm, client=client, max_steps=30)

async def run_agent_query(query: str):
    """
        Executa consulta no MCP Agent.
    """
    agent = create_agent()
    full_query = (
        "A tabela é `carros`, com colunas `marca`, `modelo`, `cor`, `ano`, `combustivel`, `preco`. "
        f"{query}"
    )
    try:
        result = await agent.run(full_query)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
