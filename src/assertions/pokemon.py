from assertions.common import verify_entity_name, verify_named_resources
from assertions.utils.allure import step
from constants import Endpoints
from db.models.ability import AbilityModel
from db.models.pokemon import PokemonModel
from hamcrest import assert_that, equal_to


@step
def _verify_pokemon_id(pokemon, expected_id):
    assert_that(pokemon["id"], equal_to(expected_id))


@step
def verify_pokemon_response(
    response, expected_pokemon: PokemonModel, expected_abilities: list[AbilityModel]
):
    _verify_pokemon_id(response, expected_pokemon.id)
    verify_entity_name(response, expected_pokemon.name)
    abilities_named_resources = [item["ability"] for item in response["abilities"]]
    verify_named_resources(
        abilities_named_resources, expected_abilities, Endpoints.ABILITY_BY_ID
    )
