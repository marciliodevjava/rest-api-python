from sqlalchemy import Column, String, Float, Integer, ForeignKey

from sql_alchemy import Base, session


class HotelModel(Base):
    __tablename__ = 'hoteis'
    hotel_id = Column(String, primary_key=True)
    nome = Column(String(80))
    estrelas = Column(Float(precision=1))
    diaria = Column(Float(precision=2))
    cidade = Column(String(45))
    site_id = Column(Integer, ForeignKey('sites.site_id'))

    #    site = relationship('SitesModel')

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade, site_id):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        self.site_id = site_id

    def json(self):
        return {
            'hotel_id': str(self.hotel_id),
            'nome': str(self.nome),
            'estrelas': float(self.estrelas),
            'diaria': float(self.diaria),
            'cidade': str(self.cidade),
            'site_id': int(self.site_id)
        }

    def salva_hotel(self):
        session.add(self)
        session.commit()

    @classmethod
    def busca_hotel(cls, hotel_id):
        hotel = session.query(cls).filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel

        return None
