from flask_restful import Resource

from enuns.message import MessagensSites
from models.sites import SitesModel
from sql_alchemy import session


class Sites(Resource):
    def get(self):
        sites = session.query(SitesModel).all()
        site = [site.json() for site in sites]
        if sites:
            return {'Sites': site}
        return {'message': MessagensSites.SITES_NAO_ENCONTRATOS}
