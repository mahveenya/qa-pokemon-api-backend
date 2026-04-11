from assertions.pokemon_list import (
    verify_pokemon_list_response,
)
from constants import DefaultValues
from tests.base_test import BaseTest


class TestPokemonList(BaseTest):
    def test_default_pokemon_list_response(self):
        response = self.client.pokemon_list.get()
        expected_count = self.db.pokemon.count_all_entries()
        expected_pokemons_ordered_by_id = self.db.pokemon.get_all(
            limit=DefaultValues.DEFAULT_POKEMON_LIMIT_PER_PAGE, order_by="id"
        )
        expected_pagination_links = {
            "next": "/pokemon?offset=20&limit=20",
            "previous": None,
        }
        verify_pokemon_list_response(
            response,
            expected_pokemons_ordered_by_id,
            expected_count,
            expected_pagination_links,
        )
