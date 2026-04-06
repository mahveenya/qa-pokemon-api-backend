from constants import Endpoints


class PokemonEndpoint:
    def __init__(self, client):
        self.client = client
        self.path = Endpoints.POKEMON

    def get(self, id_or_name: str, **kwargs):
        return self.client.get(f"{self.path}/{id_or_name}", **kwargs)
