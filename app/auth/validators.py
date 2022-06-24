from app.pkg.exceptions import MissingDataException


def validate_login(data):
    if 'email' not in data or not data['email']:
        raise MissingDataException('email')
    if 'password' not in data or not data['password']:
        raise MissingDataException('password')
