from flask import Flask, jsonify
import os

app = Flask(__name__)

# 📥 Rota para salvar a média no arquivo
@app.route('/<filename>/<float:nota1>/<float:nota2>/<float:nota3>/<float:nota4>')
def salvar_media(filename, nota1, nota2, nota3, nota4):
    # 🎯 Cálculo da média ponderada
    media = (nota1 * 2 + nota2 * 2 + nota3 * 3 + nota4 * 3) / 10
    
    # 💾 Salvar a média no arquivo
    with open(filename, 'w') as f:
        f.write(str(round(media)))

    return jsonify(mensagem=f"Média salva com sucesso no arquivo '{filename}'")

# 📤 Rota para ler a média do arquivo
@app.route('/<filename>')
def ler_media(filename):
    if not os.path.exists(filename):
        return jsonify(erro="Arquivo não encontrado"), 404
    
    with open(filename, 'r') as f:
        media = f.read()
    
    return jsonify(media=f"Média: {media}")

# 🚀 Execução da aplicação
if __name__ == '__main__':
    app.run(debug=True)
