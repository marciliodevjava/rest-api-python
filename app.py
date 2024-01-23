from flask import Flask
from flask_restful import Api

from resources.hotel_resource import Hotel, Hoteis

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=False)
