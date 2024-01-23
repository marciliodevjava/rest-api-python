from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class HotelModel(Base):
    __tablename__ = 'hoteis'
    hotel_id = Column(String, primary_key=True)  # Removido autoincrement=True
    nome = Column(String)
    estrelas = Column(Float)
    diaria = Column(Float)
    cidade = Column(String)

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

# Configurar a conexão com o banco de dados SQLite
engine = create_engine('sqlite:///mydatabase.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)

# Configurar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()
