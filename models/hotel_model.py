from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class HotelModel(Base):
    __tablename__ = 'hoteis'
    hotel_id = Column(String, primary_key=True)
    nome = Column(String)
    estrelas = Column(Float)
    diaria = Column(Float)
    cidade = Column(String)

# Configurar a conexão com o banco de dados SQLite
engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)

# Configurar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()
