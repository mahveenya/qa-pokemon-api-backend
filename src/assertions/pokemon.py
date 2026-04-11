from assertions.common import verify_id, verify_name, verify_named_resources
from assertions.utils.allure import step
from constants import Endpoints
from db.models.ability import AbilityModel
from db.models.pokemon import PokemonModel


@step
def verify_pokemon_response(
    response, expected_pokemon: PokemonModel, expected_abilities: list[AbilityModel]
):
    verify_id(response, expected_pokemon.id)
    verify_name(response, expected_pokemon.name)
    abilities_named_resources = [item["ability"] for item in response["abilities"]]
    verify_named_resources(
        abilities_named_resources, expected_abilities, Endpoints.ABILITY_BY_ID
    )
