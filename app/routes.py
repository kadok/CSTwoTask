import asyncio
from flask import Blueprint, jsonify, request, render_template
from app.data.database import SessionLocal
from app.data.models import Car
from app.agent import run_agent_query

bp = Blueprint("api", __name__, static_folder='static')

@bp.route('/api/query', methods=['POST'])
def handle_query():
    """
        Função responsável por postar as respostas obtido através das queries geradas pela LLM para a base de dados de forma assíncrona.
    """
    data = request.json
    if not data or 'query' not in data:
        return jsonify({"status": "error", "message": "Nenhuma busca foi realizada."}), 400
    
    query = data['query']
    
    # Roda a função assíncrona no Flask
    result = asyncio.run(run_agent_query(query))
    return jsonify(result)

@bp.route('/')
def index():
    """
        Renderiza a página inicial
    """
    return render_template('index.html')
