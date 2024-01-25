from my_custom_json_encoder import CustomJSONEncoder
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.hotel_resource import Hotel, Hoteis
from resources.usuario_resource import Usuario, Usuarios, UsuarioRegistro, UsuarioLogin
from sql_alchemy import Base, engine

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '123'
jwt = JWTManager(app)
app.json_encoder = CustomJSONEncoder
api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuario/<int:user_id>')
api.add_resource(UsuarioRegistro, '/cadastro')
api.add_resource(UsuarioLogin, '/login')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=False)
