import sqlite3

from flask import request
from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restful import Resource, reqparse
from jwt import ExpiredSignatureError

from enuns.message import MessagensEnumHotel
from filtros.filtros import FiltroHotel
from models.hotel_model import HotelModel
from sql_alchemy import session


class Hoteis(Resource):
    def retorna_filtros(self):
        cidade = request.args.get('cidade')
        estrelas_min = request.args.get('estrelas_min', type=float)
        diaria_min = request.args.get('diaria_min', type=float)
        diaria_max = request.args.get('diaria_max', type=float)
        offset = request.args.get('offset', type=int)
        limit = request.args.get('limit', type=int)

        return {
            'cidade': cidade,
            'estrelas_min': estrelas_min,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'offset': offset,
            'limit': limit
        }

    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()

        dados = self.retorna_filtros()
        dados_validos = {chave: dados[chave] for chave in dados if dados[chave] is not None}

        filtro = FiltroHotel.normalize_path_params(**dados_validos)
        offset = FiltroHotel.normalize_filter_offset(**dados_validos)
        limit = FiltroHotel.normalize_filter_limit(**dados_validos)

        if filtro:
            hotel = session.query(HotelModel).order_by(HotelModel.nome).filter_by(**filtro).offset(offset).limit(
                limit).all()
            if hotel:
                hoteis = [hoteis.json() for hoteis in hotel]
                return {'Hoteis': hoteis}
            else:
                return {'message': MessagensEnumHotel.HOTEL_SOLICITACAO_SEM_CONTEUDO}
        else:
            hotel = session.query(HotelModel).order_by(HotelModel.nome).offset(offset).limit(limit).all()
        hoteis = [hoteis.json() for hoteis in hotel]
        return {'Hoteis': hoteis}


class Hotel(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('nome', type=str, required=True, help=MessagensEnumHotel.MENSAGEM_PARANS_NOME)
        self.__parser.add_argument('estrelas', type=float, required=True,
                                   help=MessagensEnumHotel.MENSAGEM_PARANS_ESTRELAS)
        self.__parser.add_argument('diaria', type=float, required=True, help=MessagensEnumHotel.MENSAGEM_PARANS_DIARIA)
        self.__parser.add_argument('cidade', type=str, required=True, help=MessagensEnumHotel.MENSAGEM_PARANS_CIDADE)
        self.__parser.add_argument('site_id', type=int, required=True, help=MessagensEnumHotel.MENSAGEM_PARANS_SITE)

    def get(self, hotel_id):
        hotel = session.query(HotelModel).filter_by(hotel_id=hotel_id).first()
        if hotel:
            return {'hotel': hotel.json()}
        return {'message': MessagensEnumHotel.HOTEL_NOT_FOUND}, 404

    @jwt_required()
    def post(self, hotel_id):
        dados = self.__parser.parse_args()

        if not hotel_id:
            return {'message': MessagensEnumHotel.HOTEL_COM_NAO_PODE_NULO}, 400

        hotel_objeto = HotelModel(hotel_id, **dados)
        hotel = HotelModel.busca_hotel(hotel_id)
        if hotel:
            return {'message': MessagensEnumHotel.HOTEL_EXISTE_NA_BASE_DE_DADO,
                    'hotel': hotel.json()}, 200

        try:
            session.add(hotel_objeto)
            session.commit()
        except Exception as e:
            return {'message': MessagensEnumHotel.HOTEL_OCOREU_ERRO_GRAVAR_INFORMACAO}, 500
        except ExpiredSignatureError as e:
            return {'message': MessagensEnumHotel.HOTEL_TOKEN_EXPIRADO}, 500
        return {'message': MessagensEnumHotel.HOTEL_ADICIONADO_COM_SUCESSO,
                'hotel': hotel_objeto.json()}, 201

    @jwt_required()
    def put(self, hotel_id):
        dados = self.__parser.parse_args()

        hotel = HotelModel.busca_hotel(hotel_id)
        hotel_objeto = HotelModel(hotel_id, **dados)

        if hotel:
            hotel.nome = dados['nome']
            hotel.estrelas = dados['estrelas']
            hotel.diaria = dados['diaria']
            hotel.cidade = dados['cidade']
            hotel.site_id = dados['site_id']
            try:
                session.commit()
            except:
                return {'message': MessagensEnumHotel.HOTEL_OCOREU_ERRO_GRAVAR_INFORMACAO}, 500
            return {'hotel': hotel_objeto.json()}, 200
        else:
            try:
                session.add(hotel_objeto)
                session.commit()
            except NoAuthorizationError as e:
                return {'message': MessagensEnumHotel.HOTEL_TOKEN_EXPIRADOO}, 500
            except Exception as e:
                return {'message': MessagensEnumHotel.HOTEL_OCOREU_ERRO_GRAVAR_INFORMACAO}, 500
            return {'hotel': hotel_objeto.json()}, 201

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.busca_hotel(hotel_id)
        if hotel:
            try:
                session.delete(hotel)
                session.commit()
            except Exception as e:
                return {'message': MessagensEnumHotel.HOTEL_ERRO_DELETAR_INFORMACAO}, 500
            return {'mensagem': MessagensEnumHotel.HOTEL_REMOVIDO_COM_SUCESSO}

        return {'mensagem': MessagensEnumHotel.HOTEL_NOT_FOUND}, 404
