from flask_restful import Resource, reqparse

from enuns.message import MessagensEnumSites
from mapper.site_mapper import SiteMapper
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
        site = SitesModel.buscar_site_url(url)
        if site:
            return {'Site': site.json()}, 200
        return {'message': MessagensEnumSites.SITES_NAO_ENCONTRATOS}

    def post(self):
        dados = self.__sites_parans.parse_args()
        site = SiteMapper.mapear_site(dados)
        if site:
            try:
                site = SitesModel(site)
                session.add(site)
                session.commit()
                return {'Site': site.json()}
            except:
                return {'message': MessagensEnumSites.SITE_ERRO_AO_SALVAR_SITE}
        return {'message': MessagensEnumSites.SITE_ERRO_ENVIAR_PARAMETROS}

    def delete(self, site_id):
        site = SitesModel.buscar_site_id(site_id)
        if site:
            result = SitesModel.deletar_site_id(site)
            if result:
                return {'message': MessagensEnumSites.SITE_DELETADO_COM_SUCESSO}
            return {'message': MessagensEnumSites.SITE_OCORREU_UM_ERRO_DELETAR}
        return {'message': MessagensEnumSites.SITE_NÃO_ENCONTRATO_PARA_DELETAR}
