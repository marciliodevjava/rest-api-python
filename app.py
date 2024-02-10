from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from my_custom_json_encoder import CustomJSONEncoder
from resources.hotel_resource import Hotel, Hoteis
from resources.site_resource import Sites, Site
from resources.usuario_resource import Usuario, Usuarios, UsuarioRegistro, UsuarioLogin, UserLogout
from sql_alchemy import Base, engine

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '123'
app.config['JWT_BLACKLIST_ENABLE'] = True
jwt = JWTManager(app)
app.json_encoder = CustomJSONEncoder
api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuario/<int:user_id>')
api.add_resource(UsuarioRegistro, '/cadastro')
api.add_resource(UsuarioLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Sites, "/sites")
api.add_resource(Site, "/site/<string:url>", endpoint='get')
api.add_resource(Site, "/site", endpoint='post')
api.add_resource(Site, "/site/<int:site_id>", endpoint='delete')

BLACKLIST = set()


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_data):
    return jwt_data['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_revoked_callback(jwt_header, jwt_data):
    BLACKLIST.add(jwt_data['jti'])
    return jsonify({'message': 'Token has been revoked'}), 401


@jwt.expired_token_loader
def token_expired_token_loader(jwt_data):
    BLACKLIST.add(jwt_data['jti'])
    return jsonify({'message': 'Token has been expired'}), 401

@jwt.invalid_token_loader
def token_invalid_token_loader(jwt_data):
    BLACKLIST.add(jwt_data['jti'])
    return jsonify({'message': 'Token has been expired'}), 401

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=False)
