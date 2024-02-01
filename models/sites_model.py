from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from sql_alchemy import Base, session

class SitesModel(Base):
    __tablename__ = 'sites'
    site_id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    url = Column(String(255))
    hoteis_id = relationship('HotelModel')  # list de objetos hoteis

    def __init__(self, nome, url):
        self.nome = nome
        self.url = url

    def json(self):
        return {
            'site_id': self.site_id,
            'nome': self.nome,
            'url': self.url,
            'hoteis': [hotel.json() for hotel in self.hoteis_id]
        }

    @classmethod
    def buscar_site_id(cls, site_id):
        site = session.query(cls).filter_by(site_id=site_id).first()
        if site:
            return site
        return None

    @classmethod
    def buscar_site_url(cls, url):
        site = session.query(cls).filter_by(url=url).first()
        if site:
            return site
        return None

    @classmethod
    def deletar_site_id(cls, site):
        try:
            session.delete(site)
            session.commit()
            return True
        except:
            return None
