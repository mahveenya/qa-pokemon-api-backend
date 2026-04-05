from constants import DefaultValues
from matchers.pokemons_list import verify_pokemon_quantity
from tests.base_test import BaseTest


class TestPokemonsList(BaseTest):
    def test_default_pokemon_quantity_is_returned(self):
        res = self.pokemons_list.get()
        verify_pokemon_quantity(res, expected_quantity=DefaultValues.DEFAULT_LIMIT)
