from sqlalchemy import Column, String, Integer

from sql_alchemy import Base, session


class SitesModel(Base):
    __table__ = 'sites'
    site_id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    url = Column(String(255))

    def __init__(self, nome, url):
        self.nome = nome
        self.url = url

    def json(self):
        return {
            'site_id': self.site_id,
            'nome': self.nome,
            'url': self.url,
            'hoteis': []
        }

    @classmethod
    def buscar_sites(cls, site_id):
        site = session.query(cls).filter_by(site_id).first()
        if site:
            return site
        return None
