from flask import Flask

from flask_graphql_auth import create_access_token, create_refresh_token, get_jwt_data

from tests.util import request


def test_query_jwt_required(flask_app: Flask):
    test_cli = flask_app.test_client()

    with flask_app.test_request_context():
        access_token = create_access_token('username')

    response = request(test_cli,
                       "query",
                       f'protected(token:"{access_token}")',
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
                       f'protected(token:"{access_token}")',
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
                       f'refresh(refreshToken:"{refresh_token}")',
                       """newToken""")

    with flask_app.test_request_context():
        assert get_jwt_data(response['refresh']["newToken"], "access")["identity"] == "username"


