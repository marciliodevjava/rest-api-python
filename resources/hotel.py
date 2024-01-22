from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Brabo Hotel',
        'estrelas': 4.8,
        'diaria': 380.90,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Brasilia'
    },
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('nome', type=str)
        self.__parser.add_argument('estrelas', type=float)
        self.__parser.add_argument('diaria', type=float)
        self.__parser.add_argument('cidade', type=str)

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel != None:
            return {'Hotel': hotel}

        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        dados = self.__parser.parse_args()

        hotel_objeto = HotelModel(hotel_id, **dados)
        # novo_hotel = {'hotel_id': hotel_id, **dados}
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return {'menssagem': 'Hotel já existe na base de dados', 'Hotel': hotel}, 200
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return {'hotel': novo_hotel}, 201

    def put(self, hotel_id):
        dados = self.__parser.parse_args()

        hotel = Hotel.find_hotel(hotel_id)
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        #novo_hotel = {'hotel_id': hotel_id, **dados}
        if hotel:
            hotel.update(novo_hotel)
            return {'Hotel': hotel}, 200
        else:
            hoteis.append(novo_hotel)
            return {'Hotel': novo_hotel}, 201

    def delete(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hoteis.remove(hotel)
            return {'menssagem': 'Hotel removido com sucesso'}
        return {'menssagem': 'Hotel not found'}, 404

    @staticmethod
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel_id == hotel['hotel_id']:
                return hotel
        return None
