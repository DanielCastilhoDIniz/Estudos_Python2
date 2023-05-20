from flask_restful import Resource


lista_habilidades = ['python', 'Java', 'Ruby']


class Habilidades(Resource):

    def get(self):
        return lista_habilidades
    
    def put(self):
        lista_habilidades.append(self)
        return lista_habilidades
