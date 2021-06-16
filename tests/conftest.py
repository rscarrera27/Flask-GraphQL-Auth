import pytest

from flask import Flask
import graphene
from flask_graphql_auth import GraphQLAuth
from flask_graphql import GraphQLView

from examples.basic import Mutation, Query


@pytest.fixture(scope="function")
def flask_app():
    app = Flask(__name__)
    auth = GraphQLAuth(app)

    app.config["JWT_SECRET_KEY"] = "something"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 10
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 30

    schema = graphene.Schema(query=Query, mutation=Mutation)

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )

    return app
