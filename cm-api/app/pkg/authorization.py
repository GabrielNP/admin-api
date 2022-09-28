import json
import time

from flask import current_app as app
from jwcrypto import jwk, jwt


def __generate_key(pemfile: str) -> jwk.JWK:
    with open(pemfile, 'rb') as pemfile:
        return jwk.JWK.from_pem(pemfile.read())

def __extract_claims(token: str, pemfile: str):
    key = __generate_key(pemfile)
    enc_token = jwt.JWT(key=key, jwt=token)
    signed_token = jwt.JWT(key=key, jwt=enc_token.claims)
    return json.loads(signed_token.claims)

def generate_token(user_id: str, roles: list, **kwargs):
    key = __generate_key('private.pem')

    headers = {
        'alg': 'RS256',
        'typ': 'JWT',
    }

    access_token_expiration = time.time() + 900
    claims = {
        'exp': access_token_expiration,
        'iat': time.time(),
        'iss': app.config['SERVER'],
        'sub': user_id,
        'roles': 'ADMIN' if 'is_admin' in kwargs and kwargs['is_admin'] else roles
    }

    access_token = jwt.JWT(header=headers, claims=claims)
    access_token.make_signed_token(key)

    claims['exp'] = time.time() + 1200
    claims['intended-for'] = 'refresh'
    refresh_token = jwt.JWT(header=headers, claims=claims)
    refresh_token.make_signed_token(key)

    enc_headers = {
        'alg': 'RSA-OAEP-256',
        'enc': 'A256CBC-HS512',
        'typ': 'JWE'
    }

    eaccess_token = jwt.JWT(header=enc_headers, claims=access_token.serialize())
    eaccess_token.make_encrypted_token(key)

    erefresh_token = jwt.JWT(header=enc_headers, claims=refresh_token.serialize())
    erefresh_token.make_encrypted_token(key)

    return eaccess_token.serialize(), erefresh_token.serialize(), access_token_expiration

def verify_token(token: str, scope: str = None) -> bool:
    try:
        claims = __extract_claims(token, 'private.pem')
    except Exception as e:
        return False
    
    if ('intended-for' in claims and claims['intended-for'] == 'refresh') or claims['iss'] != app.config['SERVER']:
        return False
    
    if not scope:
        return True

    # TODO: verify scope
    

    return True
