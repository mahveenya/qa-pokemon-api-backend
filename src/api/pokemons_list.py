from constants import Endpoints


class PokemonsListEndpoint:
    def __init__(self, client):
        self.client = client
        self.path = Endpoints.ROOT

    def get(self, **kwargs):
        return self.client.get(self.path, **kwargs)
