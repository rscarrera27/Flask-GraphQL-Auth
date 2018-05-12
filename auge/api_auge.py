import datetime
from jwt import algorithms, utils

default_header = {
  "alg": "HS256",
  "typ": "JWT"
}


def make_signature(header, payload, secret):
    header = utils.base64url_encode(header)
    payload = utils.base64url_encode(payload)

    segement = header+b'.'+payload

    HS256 = algorithms.get_default_algorithms()['HS256']
    key = HS256.prepare_key(secret)
    signature = HS256.sign(segement, key)

    return signature


def create_token(identity, exp, key, **claims):
    pass


def create_refresh_token(identity, exp, key, **user):
    pass


def create_access_token(identity, exp, key, **user):
    pass


def decode_token(token, secret):
    pass


def get_token(token, secret):
    pass
