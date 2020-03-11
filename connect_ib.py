from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json

connect_ib = Flask(__name__)
api = Api(connect_ib)

class Status(Resource):
    def post(self):
        # será passado um intervalo de tempo para realizar ping na api IB? 
        response = {'status':'teste'}
        return jsonify(response)

class Trade(Resource):
    def post(self):
        response = {'trade':'teste'}
        return jsonify(response)

class Price(Resource):
    def post(self):
        response = {'price':'teste'}
        return jsonify(response)


api.add_resource(Status,'/ib/status')
api.add_resource(Trade,'/ib/trade')
api.add_resource(Price,'/ib/price')

if __name__ == '__main__':
    connect_ib.run(debug=True)
