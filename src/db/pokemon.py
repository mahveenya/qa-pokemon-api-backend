class PokemonTable:
    def __init__(self, client):
        self.client = client

    def count_all_entries(self):
        return self.client.count_all_entries("pokemon")
