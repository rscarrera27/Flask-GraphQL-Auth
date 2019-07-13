class JWTExtendedException(Exception):
    """
    Base except which all flask_graphql_auth errors extend
    """

    pass


class JWTDecodeError(JWTExtendedException):
    """
    An error decoding a JWT
    """

    pass


class NoAuthorizationError(JWTExtendedException):
    """
    An error raised when no authorization token was found in a protected endpoint
    """

    pass


class WrongTokenError(JWTExtendedException):
    """
    Error raised when attempting to use a refresh token to access an endpoint
    or vice versa
    """

    pass


class RevokedTokenError(JWTExtendedException):
    """
    Error raised when a revoked token attempt to access a protected endpoint
    """

    pass
