import datetime
import time
import uuid
import json
from jwt import algorithms, utils, exceptions
from .type_auge import TokenData

default_header = {
  "alg": "HS256",
  "typ": "JWT"
}


def make_signature(header, payload, secret):
    segement = header+b'.'+payload

    HS256 = algorithms.get_default_algorithms()['HS256']
    key = HS256.prepare_key(secret)
    signature = HS256.sign(segement, key)

    return signature


def create_token(type, identity, exp, key, **claims):
    now = int(time.time())
    exp = int(exp.total_seconds())
    payload = dict(
        type=type,
        jti=uuid.uuid4(),
        identity=identity,
        nbf=now,
        iat=now,
        exp=now + exp
    )

    for key, value in claims.items():
        payload.update({key: value})

    header = utils.base64url_encode(str(default_header).encode())
    payload = utils.base64url_encode(str(payload).encode())
    signature = make_signature(header, payload, key)
    signature= utils.base64url_encode(signature)

    token = header + b'.' + payload + b'.' + signature

    return token


def create_refresh_token(identity, exp, key, **user):
    pass


def create_access_token(identity, exp, key, **user):
    pass


def decode_token(token, secret):
    pass


def get_token(token, secret):
    pass
