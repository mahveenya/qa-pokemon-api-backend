from assertions.common import (
    verify_named_resources,
    verify_ordering_by_id,
    verify_quantity,
)
from assertions.utils.allure import step
from constants import Endpoints
from db.models.pokemon import PokemonModel
from hamcrest import assert_that, equal_to


@step
def verify_count(response, expected_count):
    assert_that(response["count"], equal_to(expected_count))


@step
def verify_pagination_links(
    response, expected_next_link=None, expected_previous_link=None
):
    assert_that(response["next"], equal_to(expected_next_link))
    assert_that(response["previous"], equal_to(expected_previous_link))


@step
def verify_results(response, expected_pokemons_ordered_by_id: list[PokemonModel]):
    results = response["results"]
    verify_quantity(results, expected_pokemons_ordered_by_id)
    verify_ordering_by_id(results, expected_pokemons_ordered_by_id)
    verify_named_resources(
        results, expected_pokemons_ordered_by_id, Endpoints.POKEMON_BY_ID_OR_NAME
    )


@step
def verify_pokemon_list_response(
    response,
    expected_pokemons_ordered_by_id: list[PokemonModel],
    expected_count,
    expected_pagination_links: dict,
):
    verify_count(response, expected_count)
    verify_pagination_links(
        response,
        expected_next_link=expected_pagination_links["next"],
        expected_previous_link=expected_pagination_links["previous"],
    )
    verify_results(response, expected_pokemons_ordered_by_id)
