from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Configurar a conexão com o banco de dados SQLite
engine = create_engine('sqlite:///banco.db', connect_args={'check_same_thread': False})

# Configurar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()