from flask import Blueprint, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/', methods=['GET'])
def client():
    resp = jsonify('OK CLIENTE')
    resp.status_code = 200
    return resp