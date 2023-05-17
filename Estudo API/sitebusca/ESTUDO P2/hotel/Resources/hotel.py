from flask import Flask
from flask_restful import Resource, Api


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

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return{'massege': 'Hotel not found'}, 404 # not found
    



    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass






