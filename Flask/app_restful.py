from flask_restful import Resource
from flask_restful import Api
from flask import Flask, request

import json


app = Flask(__name__)

api = Api(app)


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


class Desenvolvesor(Resource):

    def get(self, id):

        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolverdor de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        # print(response)
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Regitro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvesor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')


if __name__ == '__main__':
    app.run(debug=True)
