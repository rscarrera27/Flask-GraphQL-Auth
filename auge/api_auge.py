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
    header = json.loads(bheader.decode())
    payload = json.loads(bpayload.decode())

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
    if bsignature is not make_signature(bheader, bpayload, secret):
        raise exceptions.InvalidSignatureError('Invalid token signature')

    # expire check
    if payload['exp'] > int(time.time()):
        raise exceptions.ExpiredSignatureError('Token has been expired')

    return header, payload


def get_token(token, secret):
    pass
