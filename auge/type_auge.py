import datetime


class TokenData:

    def __init__(self, header, payload):
        self.header = header
        self.payload = payload

    @property
    def jti(self):
        return self.payload['jti']

    @property
    def identity(self):
        return self.payload['identity']

    @property
    def type(self):
        return self.payload['type']

    @property
    def exp(self):
        return datetime.datetime.fromtimestamp(self.payload['exp'])

    @property
    def iat(self):
        return datetime.datetime.fromtimestamp(self.payload['iat'])

    @property
    def header(self):
        return self.header

    def get(self, key):
        return self.payload[key]
