from flask import Flask
from flask_restful import Api

from resources.hotel_resource import Hotel, Hoteis
from resources.usuario_resource import Usuario, Usuarios, UsuarioRegistro
from sql_alchemy import Base
from sql_alchemy import engine

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuario/<int:user_id>')
api.add_resource(UsuarioRegistro, '/cadastro')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=False)
