from secrets import compare_digest

from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse

from blacklist import BLACKLIST
from enuns.message import MessagensEnumUsuario
from models.usuario_model import UsuarioModel
from sql_alchemy import session


# /usuarios
class Usuarios(Resource):
    def get(self):
        usuario = session.query(UsuarioModel).order_by(UsuarioModel.nome).all()
        usuarios = [usuarios.json() for usuarios in usuario]
        return {'Usuários': usuarios}


# /usuario/<int:user_id>
class Usuario(Resource):
    def __init__(self):
        self.__parcer = reqparse.RequestParser()
        self.__parcer.add_argument('name', type=str)
        self.__parcer.add_argument('login', type=str)
        self.__parcer.add_argument('senha', type=str)

    def get(self, user_id):
        usuario = session.query(UsuarioModel).filter_by(user_id=user_id).first()
        if usuario:
            return {'Usuário': usuario.json()}
        return {'message': MessagensEnumUsuario.ERRO_USUARIO_NOT_FOUND}, 404

    @jwt_required()
    def delete(self, user_id):
        usuario = UsuarioModel.busca_usuario(user_id)
        if usuario:
            try:
                session.delete(usuario)
                session.commit()  # Adicionado commit para confirmar a exclusão
            except:
                return {'message': MessagensEnumUsuario.ERRO_DELECAO_USUARIO}, 500
            return {'message': MessagensEnumUsuario.USUARIO_DELETADO_COM_SUCESSO.format(usuario.nome)}, 200
        return {'message': MessagensEnumUsuario.ERRO_USUARIO_NOT_FOUND}, 404


class UsuarioRegistro(Resource):
    def __init__(self):
        self.__parcer = reqparse.RequestParser()
        self.__parcer.add_argument('nome', type=str, required=None)
        self.__parcer.add_argument('login', type=str, required=True, help=MessagensEnumUsuario.MENSAGEM_PARANS_LOGIN)
        self.__parcer.add_argument('senha', type=str, required=True, help=MessagensEnumUsuario.MENSAGEM_PARANS_SENHA)

    # /cadastro
    def post(self):
        dados = self.__parcer.parse_args()
        login = session.query(UsuarioModel).filter_by(login=dados['login']).first()
        if login:
            return {'message': MessagensEnumUsuario.USUARIO_COM_LOGIN_JA_EXISTE.format(dados["login"])}, 500
        user = UsuarioModel(**dados)
        try:
            session.add(user)
            session.commit()
        except:
            return {'message': MessagensEnumUsuario.OCORREU_UM_ERRO_AO_SALVAR_USUARIO}
        return {'message': MessagensEnumUsuario.USUARIO_CRIADO_COM_SUCESSO.format(user.nome),
                'Usuário': user.json()}, 201


class UsuarioLogin(Resource):
    def __init__(self):
        self.__parcer = reqparse.RequestParser()
        self.__parcer.add_argument('login', type=str, required=True, help=MessagensEnumUsuario.MENSAGEM_PARANS_LOGIN)
        self.__parcer.add_argument('senha', type=str, required=True, help=MessagensEnumUsuario.MENSAGEM_PARANS_SENHA)

    def post(self):
        dados = self.__parcer.parse_args()
        user = UsuarioModel.busca_login(dados['login'])
        if user:
            if user and compare_digest(user.senha, dados['senha']):
                token = create_access_token(identity=user.user_id)
                return {'message': MessagensEnumUsuario.USUARIO_LOGADO_COM_SUCESSO,
                        'acces-token': token,
                        'nome': user.nome,
                        'login': user.login}, 200
            else:
                return {'message': MessagensEnumUsuario.SENHA_INCORRETA}, 404
        return {'message': MessagensEnumUsuario.USUARIO_E_SENHA_INCORRETO}, 404


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt_identity()
        BLACKLIST.add(jti)
        return jsonify(message=MessagensEnumUsuario.TOKEN_REVOGADO), 200
