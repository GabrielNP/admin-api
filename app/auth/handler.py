from flask import Blueprint, request

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('', methods=['POST',])
def login():
    data = request.get_json()
    print(data)
    return {}, 200
    
def logout():
    pass
