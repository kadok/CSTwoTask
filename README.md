# CSTwoTask

Neste projeto foi desenvolvida uma interface de chat para busca em uma base de dados (PostgreSQL) utilizando linguagem natural (LLM da OpenAI). Construída utilizando o protocolo MCP (Model Context Protocol).

## Estrutura do Projeto

```
CSTwoTask/
  app/
    data/
      __init__.py
      database.py
      models.py
      populate.py
    static/
      __init__.py
      favicon.ico
      index.html
      script.js
      style.css
    __init__.py
    agent.py
    config.py
    routes.py
  tests/
    __init__.py
    test_agent.py
  .env.example
  LICENSE.txt
  README.md
  requirements.txt
  run.py
```


## Requisitos

- Python 3.11+
- Flask
- LangChain OpenAI
- Postgre MCP
- Faker
- SQLAlchemy
- PyTest


## Instalação

1. Para executar este projeto é necessário instalar o PostgreSQL

```bash
sudo apt install postgresql postgresql-contrib
```

2. Crie um usuário e uma base de dados

```bash
sudo -u postgres psql -c "CREATE USER usuario WITH PASSWORD 'senha';"
sudo -u postgres createdb c2s
```

3. Caso tenha problemas com o pacote psycopg2 instale a libpq-dev

```bash
sudo apt-get install build-essential libpq-dev
```

4. Clone o repositório e navegue até o diretório


5. Utilize um ambiente virtual (Virtualenv (venv)) para a configuração do ambiente de desenvolvimento

```bash
python3 -m venv .venv
source .venv/bin/activate
```

6. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

7. Copie o arquivo .env.example e renomeie para .env. No arquivo .env defina as variáveis da conexão da base de dados e da API da OpenAI

```
OPENAI_API_KEY= sua chave da api
OPENAI_MODEL= o modelo de sua preferência
DB_LINK=postgresql://usuario:senha@localhost:5432/nomedabasededados'
```

8. Execute o script populate.py para popular a base de dados

```bash
python -m app.data.populate
```

## Execução

1. Iniciar a aplicação Flask:

```bash
python run.py
```

2. Abra o navegador e acesse a seguinte URL:

```
http://localhost:5000
```

3. Faça perguntas para sua base de dados!