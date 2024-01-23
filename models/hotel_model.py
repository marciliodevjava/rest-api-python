from sqlalchemy import Column, String, Float

from sql_alchemy import Base


class HotelModel(Base):
    __tablename__ = 'hoteis'
    hotel_id = Column(String, primary_key=True)  # Removido autoincrement=True
    nome = Column(String(80))
    estrelas = Column(Float(precision=1))
    diaria = Column(Float(precision=2))
    cidade = Column(String(45))

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id  # Modificado para usar o nome da coluna diretamente
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': str(self.hotel_id),
            'nome': str(self.nome),
            'estrelas': float(self.estrelas),
            'diaria': float(self.diaria),
            'cidade': str(self.cidade)
        }
