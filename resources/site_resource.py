from flask_restful import Resource, reqparse

from enuns.message import MessagensEnumSites
from models.sites import SitesModel
from sql_alchemy import session


class Sites(Resource):
    def get(self):
        sites = session.query(SitesModel).all()
        site = [site.json() for site in sites]
        if sites:
            return {'Sites': site}
        return {'message': MessagensEnumSites.SITES_NAO_ENCONTRATOS}


class Site(Resource):
    def __init__(self):
        self.__sites_parans = reqparse.RequestParser()
        self.__sites_parans.add_argument('url', type=str, required=True, help=MessagensEnumSites.MENSAGEM_PARANS_URL)
        self.__sites_parans.add_argument('nome', type=str, required=True, help=MessagensEnumSites.MENSAGEM_PARANS_NOME)

    def get(self, url):
        pass

    def post(self, url):
        pass
