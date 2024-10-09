from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id': 1, 'titulo': 'O Retrato de Dorian Gray', 'autor': 'Oscar Wilde', 'ano_de_publicacao': 1891, 'imagem': ''},
    {'id': 2, 'titulo': 'Saboroso Cadaver', 'autor': 'Agustina Bazterrica', 'ano_de_publicacao': 2022, 'imagem': ''},
    {'id': 3, 'titulo': 'Lugares Escuros', 'autor': 'Gillian Flynn', 'ano_de_publicacao': 2009, 'imagem': ''},
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:livro_id>', methods=['GET'])
def obter_livro(livro_id):
    livro = next((l for l in livros if l['id'] == livro_id), None)
    return jsonify(livro) if livro else ('', 404)

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route('/livros/<int:livro_id>', methods=['PUT'])
def atualizar_livro(livro_id):
    livro = next((l for l in livros if l['id'] == livro_id), None)
    if livro:
        dados = request.get_json()
        livro.update(dados)
        return jsonify(livro)
    return ('', 404)

@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    global livros
    livros = [l for l in livros if l['id'] != livro_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
