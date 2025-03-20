from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Função para carregar as tarefas de um arquivo JSON
def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as f:
            return json.load(f)
    return []

# Função para salvar as tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as f:
        json.dump(tarefas, f, indent=4)

# Endpoint para listar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = carregar_tarefas()
    return jsonify(tarefas)

# Endpoint para exibir uma tarefa específica
@app.route('/tarefas/<int:id>', methods=['GET'])
def exibir_tarefa(id):
    tarefas = carregar_tarefas()
    tarefa = next((t for t in tarefas if t['id'] == id), None)
    if tarefa:
        return jsonify(tarefa)
    else:
        return jsonify({'message': 'Tarefa não encontrada'}), 404

# Endpoint para criar uma nova tarefa
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    tarefas = carregar_tarefas()
    novo_id = max([t['id'] for t in tarefas], default=0) + 1
    tarefa = {
        'id': novo_id,
        'descricao': dados['descricao'],
        'concluida': False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    return jsonify(tarefa), 201

# Endpoint para atualizar uma tarefa existente
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()
    tarefas = carregar_tarefas()
    tarefa = next((t for t in tarefas if t['id'] == id), None)
    
    if tarefa:
        tarefa['descricao'] = dados.get('descricao', tarefa['descricao'])
        tarefa['concluida'] = dados.get('concluida', tarefa['concluida'])
        salvar_tarefas(tarefas)
        return jsonify(tarefa)
    else:
        return jsonify({'message': 'Tarefa não encontrada'}), 404

# Endpoint para excluir uma tarefa
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    tarefas = carregar_tarefas()
    tarefa = next((t for t in tarefas if t['id'] == id), None)
    
    if tarefa:
        tarefas.remove(tarefa)
        salvar_tarefas(tarefas)
        return jsonify({'message': 'Tarefa excluída com sucesso'})
    else:
        return jsonify({'message': 'Tarefa não encontrada'}), 404

# Função principal para rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
