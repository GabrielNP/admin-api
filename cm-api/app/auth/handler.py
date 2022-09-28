from flask import Blueprint, request

from app.pkg import response
from app.pkg.exceptions import ForbiddenException, MissingDataException


auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('', methods=['POST',])
def login():
    from app.auth.usecases import login_uc
    from app.auth.validators import validate_login

    try:
        data = request.get_json()
        validate_login(data)
        user = login_uc(data)
        return response.success('success', user)
    except Exception as e:
        if isinstance(e, MissingDataException):
            return response.error(e.message, 'fail to login')
        if isinstance(e, ForbiddenException):
            return response.forbidden()
        return response.error(f'{e}', 'fail to login')
    
def logout():
    pass

@auth_bp.route('/encrypt', methods=['POST',])
def encrypt():
    from app.pkg import crypt

    data = request.get_json()
    message = crypt.Crypt(data['message']).encrypt()
    return response.success('ok', message)
