import asyncio
from flask import Blueprint, jsonify, request, render_template
from app.data.database import SessionLocal
from app.data.models import Car
from app.agent import run_agent_query

bp = Blueprint("api", __name__, static_folder='static')

@bp.route('/api/query', methods=['POST'])
def handle_query():
    data = request.json
    if not data or 'query' not in data:
        return jsonify({"status": "error", "message": "Nenhuma busca foi realizada."}), 400
    
    query = data['query']
    
    # Run the async function in the Flask context
    result = asyncio.run(run_agent_query(query))
    return jsonify(result)

@bp.route('/')
def index():
    return render_template('index.html')
