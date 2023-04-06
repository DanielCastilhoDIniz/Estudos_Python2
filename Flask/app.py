""" criando primeira API em Flask"""
import json
from flask import Flask, jsonify, request


app = Flask(__name__)


# @app.route("/<int:id>")
# def pessoas(id):
#     return jsonify({'id': id, 'nome': 'Daniel', 'profissão': 'Desenvolvedor'})


@app.route("/soma" , methods=["POST"])


def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma': total})


if __name__ == "__main__":
    app.run(debug=True)
