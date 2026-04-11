from constants import Endpoints


class PokemonListEndpoint:
    def __init__(self, client):
        self.client = client
        self.path = Endpoints.POKEMON

    def get(self, **kwargs):
        return self.client.get(self.path, **kwargs)
