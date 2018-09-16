import graphene


class ResponseMessageField(graphene.ObjectType):
    message = graphene.String()