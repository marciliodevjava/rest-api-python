from flask_restful import Resource, reqparse

from models.usuario_model import UsuarioModel
from sql_alchemy import session


class Usuarios(Resource):
    def get(self):
        usuario = session.query(UsuarioModel).filter_by(UsuarioModel.nome).all()
        usuarios = [usuarios.json() for usuarios in usuario]
        return {'Usuários': usuarios}


class Usuario(Resource):
    def __init__(self):
        self.__parcer = reqparse.RequestParser()
        self.__parcer.add_argument('name', type=str)
        self.__parcer.add_argument('login', type=str)
        self.__parcer.add_argument('senha', type=str)

    def get(self, user_id):
        usuario = session.query(UsuarioModel).filter_by(user_id=user_id).first()
        if usuario:
            return {'Usuário': usuario}
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        usuario = UsuarioModel.busca_usuario(user_id)
        if usuario:
            try:
                session.delete(usuario)
            except:
                return {'message': 'Ocoreu um erro ao deletar o usuário'}, 500
            return {'message': f'Usuário {usuario.nome} deletado com sucesso!'}
        return {'message': 'Usuario not found'}, 404
