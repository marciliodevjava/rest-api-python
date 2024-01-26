from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from sql_alchemy import Base, session


class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    user_id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    login = Column(String(40))
    senha = Column(String(100))
    data = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'nome': self.nome,
            'login': self.login,
            'data': self.data.strftime("%Y-%m-%d %H:%M:%S")
        }

    @classmethod
    def busca_usuario(cls, user_id):
        usuario = session.query(cls).filter_by(user_id=user_id).first()
        return usuario

    @classmethod
    def busca_login(cls, login):
        usuario = session.query(cls).filter_by(login=login).first()
        return usuario
