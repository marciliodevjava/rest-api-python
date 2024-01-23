from flask_restful import Resource, reqparse
from models.hotel_model import HotelModel, session

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
        hotel = self.find_hotel(hotel_id)
        if hotel:
            return {'hotel': hotel.json()}

        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        dados = self.__parser.parse_args()

        # Verifica se o 'hotel_id' foi passado corretamente
        if not hotel_id:
            return {'mensagem': 'O campo hotel_id não pode ser nulo'}, 400

        hotel_objeto = HotelModel(hotel_id, **dados)
        new_hotel = hotel_objeto.json()
        hotel = session.query(HotelModel).filter_by(hotel_id=hotel_id).first()
        if hotel:
            return {'mensagem': 'Hotel já existe na base de dados', 'hotel': hotel.json()}, 200

        session.add(hotel_objeto)
        session.commit()

        return {'mensagem': 'Hotel adicionado com sucesso', 'hotel': new_hotel}, 201

    def put(self, hotel_id):
        dados = self.__parser.parse_args()

        hotel = self.find_hotel(hotel_id)
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        if hotel:
            hotel.update(novo_hotel)
            return {'hotel': hotel.json()}, 200
        else:
            hoteis.append(novo_hotel)
            return {'hotel': novo_hotel}, 201

    def delete(self, hotel_id):
        hotel = self.find_hotel(hotel_id)
        if hotel:
            hoteis.remove(hotel.json())
            return {'mensagem': 'Hotel removido com sucesso'}
        return {'mensagem': 'Hotel not found'}, 404

    def find_hotel(self, hotel_id):
        hotel = session.query(HotelModel).filter_by(hotel_id=hotel_id).first()
        return hotel