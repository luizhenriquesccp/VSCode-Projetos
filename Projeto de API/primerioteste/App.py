from flask import Flask, jsonify, request

app = Flask(__name__)

livros2 = [
    {'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'ano': 1954},
    {'id': 2, 'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949}, 
    {'id': 3, 'titulo': 'O Hobbit', 'autor': 'J.R.R. Tolkien', 'ano': 1937},
    {'id': 4, 'titulo': 'Fahrenheit 451', 'autor': 'Ray Bradbury', 'ano': 1953}
]

@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros2)

@app.route('/livros/<int:id>', methods=['GET'])
def get_livro_por_id(id):
    for livro in livros2:
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({'erro': 'Livro não encontrado'}), 404

app.run(port=5000, host="localhost", debug=True)