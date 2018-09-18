from flask import _app_ctx_stack as ctx_stack, current_app
from functools import wraps
import jwt

from .exceptions import *
from .fields import *


def decode_jwt(encoded_token, secret, algorithm, identity_claim_key,
               user_claims_key):
    """
    Decodes an encoded JWT

    :param encoded_token: The encoded JWT string to decode
    :param secret: Secret key used to encode the JWT
    :param algorithm: Algorithm used to encode the JWT
    :param identity_claim_key: expected key that contains the identity
    :param user_claims_key: expected key that contains the user claims
    :return: Dictionary containing contents of the JWT
    """
    # This call verifies the ext, iat, and nbf claims
    data = jwt.decode(encoded_token, secret, algorithms=[algorithm])

    # Make sure that any custom claims we expect in the token are present
    if 'jti' not in data:
        raise JWTDecodeError("Missing claim: jti")
    if identity_claim_key not in data:
        raise JWTDecodeError("Missing claim: {}".format(identity_claim_key))
    if 'type' not in data or data['type'] not in ('refresh', 'access'):
        raise JWTDecodeError("Missing or invalid claim: type")
    if user_claims_key not in data:
        data[user_claims_key] = {}

    return data


def get_jwt_data(token, token_type):
    """
    Decodes encoded JWT token by using extension setting and validates token type

    :param token: The encoded JWT string to decode
    :param token_type: JWT type for type validation (access or refresh)
    :return: Dictionary containing contents of the JWT
    """
    jwt_data = decode_jwt(
        encoded_token=token,
        secret=current_app.config['JWT_SECRET_KEY'],
        algorithm='HS256',
        identity_claim_key=current_app.config['JWT_IDENTITY_CLAIM'],
        user_claims_key=current_app.config['JWT_USER_CLAIMS']
        )

    # token type verification
    if jwt_data['type'] != token_type:
        raise WrongTokenError('Only {} tokens are allowed'.format(token_type))

    return jwt_data


def verify_jwt_in_argument(token):
    """
    Verify access token

    :param token: The encoded access type JWT string to decode
    :return: Dictionary containing contents of the JWT
    """
    jwt_data = get_jwt_data(token, 'access')
    ctx_stack.top.jwt = jwt_data


def verify_refresh_jwt_in_argument(token):
    """
    Verify refresh token

    :param token: The encoded refresh type JWT string to decode
    :return: Dictionary containing contents of the JWT
    """
    jwt_data = get_jwt_data(token, 'refresh')
    ctx_stack.top.jwt = jwt_data


def query_jwt_required(fn):
    """
    A decorator to protect a query resolver.

    If you decorate an resolver with this, it will ensure that the requester
    has a valid access token before allowing the resolver to be called. This
    does not check the freshness of the access token.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(args[0])
        token = kwargs.pop(current_app.config['JWT_TOKEN_ARGUMENT_NAME'])
        try:
            verify_jwt_in_argument(token)
        except Exception as e:
            return AuthInfoField(message=str(e))

        return fn(*args, **kwargs)
    return wrapper


def query_jwt_refresh_token_required(fn):
    """
    A decorator to protect a query resolver.

    If you decorate an query resolver with this, it will ensure that the requester
    has a valid refresh token before allowing the resolver to be called.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = kwargs.pop(current_app.config['JWT_REFRESH_TOKEN_ARGUMENT_NAME'])
        try:
            verify_refresh_jwt_in_argument(token)
        except Exception as e:
            return AuthInfoField(message=str(e))

        return fn(*args, **kwargs)
    return wrapper


def mutation_jwt_required(fn):
    """
    A decorator to protect a mutation.

    If you decorate a mutation with this, it will ensure that the requester
    has a valid access token before allowing the mutation to be called. This
    does not check the freshness of the access token.
    """
    @wraps(fn)
    def wrapper(cls, *args, **kwargs):
        token = kwargs.pop(current_app.config['JWT_TOKEN_ARGUMENT_NAME'])
        try:
            verify_jwt_in_argument(token)
        except Exception as e:
            return cls(AuthInfoField(message=str(e)))

        return fn(cls, *args, **kwargs)
    return wrapper


def mutation_jwt_refresh_token_required(fn):
    """
    A decorator to protect a mutation.

    If you decorate anmutation with this, it will ensure that the requester
    has a valid refresh token before allowing the mutation to be called.
    """
    @wraps(fn)
    def wrapper(cls, *args, **kwargs):
        token = kwargs.pop(current_app.config['JWT_REFRESH_TOKEN_ARGUMENT_NAME'])
        try:
            verify_refresh_jwt_in_argument(token)
        except Exception as e:
            return cls(AuthInfoField(message=str(e)))

        return fn(*args, **kwargs)
    return wrapper

