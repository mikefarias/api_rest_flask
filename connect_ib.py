from flask import Flask, jsonify, request
import json

connect_ib = Flask(__name__)

#objetivo é pingar na API IB de 5 em 5 min para verificar status da bolsa
#deve ser passado intervalo de tempo ?
class Status:
    @connect_ib.route("/ib/status", methods=['POST'])
    def get_status_ib():
        response = {'status':'teste'}
        return jsonify(response)       


class Trade:
    @connect_ib.route("/ib/trade", methods=['POST'])
    def get_trade_ib():
        response = {'trade':'teste'}
        return jsonify(response)       


class Price:
    @connect_ib.route("/ib/price", methods=['POST'])
    def get_price_ib():
        response = {'price':'teste'}
        return jsonify(response)


if __name__ == '__main__':
    connect_ib.run(debug=True)
