import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from app import config
from app.agent import create_agent, run_agent_query


@pytest.fixture
def mock_config(monkeypatch):
    """
        Define variáveis de configuração falsas para os testes.
    """
    monkeypatch.setattr(config.Config, "DB_LINK", "postgresql://fake_user:fake_pass@localhost/fakedb")
    monkeypatch.setattr(config.Config, "OPENAI_MODEL", "gpt-4o-mini")


def test_create_agent_success(mock_config):
    """
        Testa se create_agent retorna um MCPAgent configurado.
    """
    with patch("app.agent.MCPClient.from_dict") as mock_client, \
         patch("app.agent.ChatOpenAI") as mock_llm, \
         patch("app.agent.MCPAgent") as mock_agent:

        fake_client = MagicMock()
        fake_llm = MagicMock()
        fake_agent = MagicMock()

        mock_client.return_value = fake_client
        mock_llm.return_value = fake_llm
        mock_agent.return_value = fake_agent

        agent_instance = create_agent()

        mock_client.assert_called_once()
        mock_llm.assert_called_once_with(model="gpt-4o-mini")
        mock_agent.assert_called_once_with(llm=fake_llm, client=fake_client, max_steps=30)

        assert agent_instance == fake_agent


def test_create_agent_missing_db_link(monkeypatch):
    """
        Testa erro se DB_LINK não está definido.
    """
    monkeypatch.setattr(config.Config, "DB_LINK", None)

    with pytest.raises(ValueError) as exc:
        create_agent()

    assert "DB_LINK não definido" in str(exc.value)


@pytest.mark.asyncio
async def test_run_agent_query_success(mock_config):
    """
        Testa run_agent_query com retorno bem-sucedido.
    """
    fake_result = {"dados": [1, 2, 3]}

    with patch("app.agent.create_agent") as mock_create_agent:
        mock_agent = MagicMock()
        mock_agent.run = AsyncMock(return_value=fake_result)
        mock_create_agent.return_value = mock_agent

        result = await run_agent_query("Selecione todos os carros")

        mock_agent.run.assert_awaited_once()
        assert result["status"] == "success"
        assert result["result"] == fake_result


@pytest.mark.asyncio
async def test_run_agent_query_error(mock_config):
    """
        Testa run_agent_query com erro na execução.
    """
    with patch("app.agent.create_agent") as mock_create_agent:
        mock_agent = MagicMock()
        mock_agent.run = AsyncMock(side_effect=Exception("Falha de conexão"))
        mock_create_agent.return_value = mock_agent

        result = await run_agent_query("Selecione todos os carros")

        assert result["status"] == "error"
        assert "Falha de conexão" in result["message"]
