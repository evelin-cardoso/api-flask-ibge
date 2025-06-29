from flask import Flask, jsonify
import json

app = Flask(__name__)

# Carrega os dados do arquivo JSON
with open("indicadores.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

@app.route('/api/municipio/<nome>', methods=['GET'])
def indicadores_municipio(nome):
    nome = nome.lower()
    if nome in dados:
        return jsonify(dados[nome])
    else:
        return jsonify({"erro": "Município não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
