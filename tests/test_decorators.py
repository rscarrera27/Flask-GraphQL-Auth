from flask import Flask

from flask_graphql_auth import create_access_token, create_refresh_token, get_jwt_data
from flask_graphql_auth.decorators import _extract_header_token_value

from tests.util import request


def test_query_jwt_required(flask_app: Flask):
    test_cli = flask_app.test_client()

    with flask_app.test_request_context():
        access_token = create_access_token('username')

    response = request(test_cli,
                       "query",
                       'protected(token:"{0}")'.format(access_token),
                       """... on AuthInfoField{
                                message
                            }
                            ... on MessageField{
                                message
                            }""")

    assert response['protected']["message"] == "Hello World!"


def test_mutation_jwt_required(flask_app: Flask):
    test_cli = flask_app.test_client()

    with flask_app.test_request_context():
        access_token = create_access_token('username')

    response = request(test_cli,
                       "mutation",
                       'protected(token:"{0}")'.format(access_token),
                       """message {
                        ... on MessageField {
                                message
                            }
                        ... on AuthInfoField {
                                message
                            }
                        }""")

    assert response['protected']["message"]["message"] == "Protected mutation works"


def test_mutation_refresh_jwt_token_required(flask_app: Flask):
    test_cli = flask_app.test_client()

    with flask_app.test_request_context():
        refresh_token = create_refresh_token('username')

    response = request(test_cli,
                       "mutation",
                       'refresh(refreshToken:"{0}")'.format(refresh_token),
                       """newToken""")

    with flask_app.test_request_context():
        assert get_jwt_data(response['refresh']["newToken"], "access")["identity"] == "username"


def test_extract_header_token_value_from_authorization_header(flask_app):
    token_value = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
    headers = {
        "Authorization": "Bearer {}".format(token_value)
    }
    with flask_app.test_request_context():
        assert _extract_header_token_value(headers) == token_value


def test_extract_header_token_value_empty(flask_app):
    with flask_app.test_request_context():
        assert _extract_header_token_value({}) == None
