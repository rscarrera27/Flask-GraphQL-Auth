# Flask-GraphQL-Auth [![PyPI version](https://badge.fury.io/py/Flask-GraphQL-Auth.svg)](https://badge.fury.io/py/Flask-GraphQL-Auth)

## Installation
```sh
pip install Flask-GraphQL-Auth
```

## usuage
```python
from flask import Flask
import graphene
from flask_graphql_auth import *
from flask_graphql import GraphQLView

app = Flask(__name__)
auth = GraphToken(app)

app.config["JWT_SECRET_KEY"] = "something"  # change this!
app.config["REFRESH_EXP_LENGTH"] = 30
app.config["ACCESS_EXP_LENGTH"] = 10


class AuthMutation(graphene.Mutation):
    class Arguments(object):
        username = graphene.String()
        password = graphene.String()

    access_token = graphene.String()
    refresh_token = graphene.String()

    def mutate(self, info, username, password):

        return AuthMutation(access_token=create_access_token(username),
                            refresh_token=create_refresh_token(username))


class ProtectedMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()

    ok = graphene.Boolean()

    @jwt_required
    def mutate(self, info, token):
        return AuthMutation(ok=True)


class RefreshMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()

    new_token = graphene.String()

    @jwt_refresh_token_required
    def mutate(self, info, token):
        current_user = get_jwt_identity()
        return RefreshMutation(new_token=create_access_token(identity=current_user))


class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    protected = ProtectedMutation.Field()


class Query(graphene.ObjectType):
    protected = graphene.String(message=graphene.String(),
                                token=graphene.String())

    @jwt_required
    def resolve_protected(self, info, token, message):
        return message


schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
        )

if __name__ == '__main__':
    app.run(debug=True)
```

## docs
coming soon
