from secrets import compare_digest

from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from enuns.message import MessagensEnum
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
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        usuario = UsuarioModel.busca_usuario(user_id)
        if usuario:
            try:
                session.delete(usuario)
            except:
                return {'message': MessagensEnum.ERRO_DELECAO_USUARIO}, 500
            return {'message': MessagensEnum.USUARIO_DELETADO_COM_SUCESSO.format(usuario.nome)}, 200
        return {'message': MessagensEnum.ERRO_USUARIO_NOT_FOUND}, 404


class UsuarioRegistro(Resource):
    def __init__(self):
        self.__parcer = reqparse.RequestParser()
        self.__parcer.add_argument('nome', type=str, required=None)
        self.__parcer.add_argument('login', type=str, required=True, help='O campo login tem que ser passado.')
        self.__parcer.add_argument('senha', type=str, required='O campo senha tem que ser passado.')

    # /cadastro
    def post(self):
        dados = self.__parcer.parse_args()
        login = session.query(UsuarioModel).filter_by(login=dados['login']).first()
        if login:
            return {'message': f'Usuário com o login {dados["login"]} já existe'}, 500
        user = UsuarioModel(**dados)
        try:
            session.add(user)
            session.commit()
        except:
            return {'message': 'Ocorreu um erro para salvar o usuário'}
        return {'message': 'USUARIO CRIADO COM SUCESSO!',
                'Usuário': user.json()}, 201


class UsuarioLogin(Resource):
    def __init__(self):
        self.__parcer = reqparse.RequestParser()
        self.__parcer.add_argument('login', type=str, required=True, help='O campo login não foi enviado')
        self.__parcer.add_argument('senha', type=str, required=True, help='O campo senha não foi envaido')

    def post(self):
        dados = self.__parcer.parse_args()
        user = UsuarioModel.busca_login(dados['login'])
        if user:
            if user and compare_digest(user.senha, dados['senha']):
                token = create_access_token(identity=user.user_id)
                return {'message': f'Usuario Logado com SUCESSO!',
                        'acces-token': token,
                        'nome': user.nome,
                        'login': user.login}, 200
            else:
                return {'message': 'Senha INCORRETA, tente novamente'}, 404
        return {'message': 'Usuario e senha incoretos!'}, 404
