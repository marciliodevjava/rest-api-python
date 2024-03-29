from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from enuns.message import MessagensEnumSites
from mapper.site_mapper import SiteMapper
from models.sites_model import SitesModel
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
        self.__sites_parans.add_argument('hoteis', type=str, required=False,
                                         help=MessagensEnumSites.MENSAGEM_PARANS_HOTEL)

    @jwt_required()
    def get(self, url):
        try:
            site = SitesModel.buscar_site_url(url)
            if site:
                return {'Site': site.json()}, 200
            return {'message': MessagensEnumSites.SITES_NAO_ENCONTRATOS}, 404
        except:
            return {'message': MessagensEnumSites.ERRO_AO_CONSULTAR_NO_BANCO}, 500

    @jwt_required()
    def post(self):
        try:
            dados = self.__sites_parans.parse_args()
            site = SiteMapper.mapear_site(**dados)
            if site:
                buscar_site = SitesModel.buscar_site_url(**dados)
                if not buscar_site:
                    try:
                        site = SitesModel(**site)
                        session.add(site)
                        session.commit()
                        return {'Site': site.json()}, 201
                    except:
                        return {'message': MessagensEnumSites.SITE_ERRO_AO_SALVAR_SITE}, 500
                return {'message': MessagensEnumSites.SITE_JA_EXISTE_NA_BASE_DE_DADOS,
                        'site': buscar_site.json()}, 400
        except:
            return {'message': MessagensEnumSites.SITE_ERRO_ENVIAR_PARAMETROS}, 500

    @jwt_required()
    def delete(self, site_id):
        site = SitesModel.buscar_site_id(site_id)
        hotel = site.hoteis_id
        if site:
            result = SitesModel.deletar_site_id(site, hotel)
            if result:
                return {'message': MessagensEnumSites.SITE_DELETADO_COM_SUCESSO}, 200
            return {'message': MessagensEnumSites.SITE_OCORREU_UM_ERRO_DELETAR}, 500
        return {'message': MessagensEnumSites.SITE_NAO_ENCONTRATO_PARA_DELETAR}, 404
