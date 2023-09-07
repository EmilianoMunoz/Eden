from flask import Blueprint, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente/', methods=['GET'])
def index():
    resp = jsonify('OK CLIENTE')
    resp.status_code = 200
    return resp