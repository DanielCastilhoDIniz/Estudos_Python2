from flask import Flask
from flask_restful import Resource, reqparse


hoteis = [
    {
        "hotel_id": "123",
        "nome": "Hotel A",
        "estrelas": 4,
        "diarias": 150.00,
        "cidade": "São Paulo"
    },
    {
        "hotel_id": "2",
        "nome": "Hotel B",
        "estrelas": 3,
        "diarias": 120.00,
        "cidade": "Rio de Janeiro"
    },
    {
        "hotel_id": "3",
        "nome": "Hotel C",
        "estrelas": 5,
        "diarias": 200.00,
        "cidade": "Belo Horizonte"
    },
    {
        "hotel_id": "4",
        "nome": "Hotel D",
        "estrelas": 4,
        "diarias": 180.00,
        "cidade": "Salvador"
    },
    {
        "hotel_id": "5",
        "nome": "Hotel E",
        "estrelas": 2,
        "diarias": 80.00,
        "cidade": "Fortaleza"
    },
    {
        "hotel_id": "6",
        "nome": "Hotel F",
        "estrelas": 3,
        "diarias": 100.00,
        "cidade": "Porto Alegre"
    }
]

# Define uma classe Hoteis que herda da classe Resource


class Hoteis(Resource):

    argumento = reqparse.RequestParser()
    argumento.add_argument('nome')
    argumento.add_argument('estrelas')
    argumento.add_argument('diarias')
    argumento.add_argument('cidade')

# Método GET para a classe Hoteis
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    # Método para encontrar um hotel pelo ID
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel

        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'massege': 'Hotel not found'}, 404  # not found

    def post(self, hotel_id):

        dados = Hotel.argumento.parse_args()  # Analisa os argumentos da requisição usando o RequestParser
        novo_hotel = {
            "hotel_id": hotel_id,
            "nome": dados['nome'],
            "estrelas": dados['estrelas'],
            "diarias": dados['diarias'],
            "cidade": dados['cidade']
        }
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumento.parse_args()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel) # Atualiza as informações do hotel com os novos dados

        pass

    def delete(self, hotel_id):
        pass
