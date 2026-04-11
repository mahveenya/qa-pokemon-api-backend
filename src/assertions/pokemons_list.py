from assertions.common import verify_named_resources
from assertions.utils.allure import step
from constants import Endpoints
from db.models.pokemon import PokemonModel
from hamcrest import assert_that, equal_to


@step
def _verify_count(res, expected_count):
    assert_that(res["count"], equal_to(expected_count))


@step
def _verify_results_count(res, expected_results_quantity):
    assert_that(len(res["results"]), equal_to(expected_results_quantity))


@step
def _verify_pagination_links(res, expected_next_link=None, expected_previous_link=None):
    assert_that(res["next"], equal_to(expected_next_link))
    assert_that(res["previous"], equal_to(expected_previous_link))


@step
def _verify_pokemons_are_ordered_by_id(
    results, expected_pokemons_ordered_by_id: list[PokemonModel]
):
    for index, expected_pokemon in enumerate(expected_pokemons_ordered_by_id):
        actual_pokemon_name = results[index]["name"]
        assert_that(actual_pokemon_name, equal_to(expected_pokemon.name))


@step
def _verify_results(response, expected_pokemons_ordered_by_id: list[PokemonModel]):
    results = response["results"]
    _verify_pokemons_are_ordered_by_id(results, expected_pokemons_ordered_by_id)
    verify_named_resources(
        results, expected_pokemons_ordered_by_id, Endpoints.POKEMON_BY_ID_OR_NAME
    )


@step
def verify_pokemons_list_response(
    response,
    expected_pokemons_ordered_by_id: list[PokemonModel],
    expected_count,
    expected_pagination_links: dict,
):
    _verify_count(response, expected_count)
    _verify_results_count(response, len(expected_pokemons_ordered_by_id))
    _verify_pagination_links(
        response,
        expected_next_link=expected_pagination_links["next"],
        expected_previous_link=expected_pagination_links["previous"],
    )
    _verify_results(response, expected_pokemons_ordered_by_id)
