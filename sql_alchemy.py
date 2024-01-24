from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Configurar a conexão com o banco de dados SQLite
engine = create_engine('sqlite:///mydatabase.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)

# Configurar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()
