import datetime
from jwt import algorithms, utils

default_header = {
  "alg": "HS256",
  "typ": "JWT"
}

def make_signature(header, payload, secret):

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
