import graphene


class AuthInfoField(graphene.ObjectType):
    message = graphene.String()