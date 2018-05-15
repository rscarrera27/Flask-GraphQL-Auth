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
    segement = header + b'.' + payload

    HS256 = algorithms.get_default_algorithms()['HS256']
    key = HS256.prepare_key(secret)
    signature = HS256.sign(segement, key)

    return signature


def create_token(type, identity, exp, key, **claims):
    now = int(time.time())
    exp = int(exp.total_seconds())
    payload = {
        "type": type,
        "jti": str(uuid.uuid4()),
        "identity": identity,
        "nbf": now,
        "iat": now,
        "exp": now + exp
    }

    for key, value in claims.items():
        payload.update({key: value})

    header = utils.base64url_encode(json.dumps(str(default_header)).encode())
    payload = utils.base64url_encode(json.dumps(str(payload)).encode())
    signature = make_signature(header, payload, key)
    signature= utils.base64url_encode(signature)

    token = header + b'.' + payload + b'.' + signature

    return token


def create_refresh_token(identity, exp, key, **user):
    refresh_token = create_token(type='refresh',
                                 identity=identity,
                                 exp=exp,
                                 key=key,
                                 **user)

    return refresh_token


def create_access_token(identity, exp, key, **user):
    access_token = create_token(type='access',
                                identity=identity,
                                exp=exp,
                                key=key,
                                **user)

    return access_token


def decode_token(token, secret):

    if type(token) is bytes:
        token = token.decode()

    bheader, bpayload, bsignature = token.split('.')
    print(json.loads(utils.base64url_decode(bpayload).decode('utf-8')))

    header = json.loads(utils.base64url_decode(bheader).decode('utf-8')).replace("'", '"')
    header = json.loads(header)

    payload = json.loads(utils.base64url_decode(bpayload).decode('utf-8')).replace("'", '"')
    payload = json.loads(payload)

    # claim check
    payload_keys = list(payload.keys())
    if 'jti' not in payload_keys:
        raise exceptions.MissingRequiredClaimError('jti')
    if 'exp' not in payload_keys:
        raise exceptions.MissingRequiredClaimError('exp')
    if 'type' not in payload_keys:
        raise exceptions.MissingRequiredClaimError('type')
    if 'identity' not in payload_keys:
        raise exceptions.MissingRequiredClaimError('identity')
    if 'iat' not in payload_keys:
        raise exceptions.MissingRequiredClaimError('iat')

    # signature compare
    _header = utils.base64url_encode(json.dumps(str(header)).encode())
    _payload = utils.base64url_encode(json.dumps(str(payload)).encode())
    print(_payload)
    if utils.base64url_decode(bsignature) is not make_signature(_header, _payload, secret):
        print(str(utils.base64url_decode(bsignature)))
        print(make_signature(_header, _payload, secret))
        raise exceptions.InvalidSignatureError('Invalid token signature')

    # expire check
    if payload['exp'] > int(time.time()):
        raise exceptions.ExpiredSignatureError('Token has been expired')

    return header, payload


def get_token(token, secret):
    header, payload = decode_token(token, secret)

    return TokenData(header, payload)


def get_access_token(token, secret):
    token = TokenData(*decode_token(token, secret))

    if TokenData.type is not 'access':
        raise exceptions.InvalidTokenError('Not access token')

    return token


def get_refresh_token(token, secret):
    token = TokenData(*decode_token(token, secret))

    if TokenData.type is not 'refresh':
        raise exceptions.InvalidTokenError('Not refresh token')

    return token
