import jwt
from datetime import datetime, timedelta


def encode_token(user_id: str):
    access_token = {
        'exp': datetime.utcnow() + timedelta(days=0, minutes=15),
        'iat': datetime.utcnow(),
        'sub': user_id
    }

    refresh_token = {
        'exp': datetime.utcnow() + timedelta(days=0, hours=2),
        'iat': datetime.utcnow(),
        'sub': user_id
    }

    encoded_access_token = jwt.encode(payload=access_token, key="secret", algorithm="HS512")
    encoded_refresh_token = jwt.encode(payload=refresh_token, key="secret", algorithm="HS512")

    return encoded_access_token, encoded_refresh_token
