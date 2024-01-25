import datetime

from sqlalchemy import Column, String, Integer

from sql_alchemy import Base, session


class UsuarioModel(Base):
    _tablename__ = 'usuarios'
    user_id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    login = Column(String(40))
    senha = Column(String(100))

    def __init__(self, nome, login, senha):
        self.__nome = nome
        self.__login = login
        self.__senha = senha

    def json(self):
        return {
            'nome': self.__nome,
            'login': self.login,
            'data': datetime.datetime.now()
        }

    @classmethod
    def busca_usuario(cls, nome):
        usuario = session.query(cls).filter_by(nome=nome).first()
        if usuario:
            return usuario
        return None
