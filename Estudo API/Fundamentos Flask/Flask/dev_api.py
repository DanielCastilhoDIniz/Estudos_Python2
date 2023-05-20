""" criando api com lista de desenvolvedores"""

import json
from flask import Flask, jsonify, request


app = Flask(__name__)


desenvolvedores = [
    {
        'id': 0,
        'nome': 'Rafael',
        'habilidades': ['Python', 'Django']
    },
    {
        'id': 1,
        'nome': 'Daniel',
        'habilidades': ['Python', 'Flask']
    }
]

# devolve um desenvoldor pelo ID, também altera e deleta


@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolverdor de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        # print(response)
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Regitro excluido'})


# lista todos os desenvolvedores

@app.route("/dev/", methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados[id] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro Inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run(debug=True)
