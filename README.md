# CSTwoTask

Neste projeto foi desenvolvida uma interface de chat para busca em uma base de dados (PostgreSQL) utilizando linguagem natural (LLM da OpenAI). Construída utilizando o protocolo MCP (Model Context Protocol).

## Estrutura do Projeto

```
CSTwoTask/
.
├── app
│   ├── agent.py
│   ├── config.py
│   ├── data
│   │   ├── database.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── populate.py
│   │   └── __pycache__
│   │       ├── database.cpython-312.pyc
│   │       ├── __init__.cpython-312.pyc
│   │       ├── models.cpython-312.pyc
│   │       └── populate.cpython-312.pyc
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── agent.cpython-312.pyc
│   │   ├── config.cpython-312.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   └── routes.cpython-312.pyc
│   ├── routes.py
│   └── static
│       ├── favicon.ico
│       ├── index.html
│       ├── __init__.py
│       ├── script.js
│       └── styles.css
├── LICENSE
├── __pycache__
│   └── run.cpython-312.pyc
├── README.md
├── requirements.txt
├── run.py
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   └── test_agent.cpython-312-pytest-8.4.1.pyc
    └── test_agent.py

9 directories, 30 files
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

4. Para executar os testes unitários
```bash
pytest -s -v
```