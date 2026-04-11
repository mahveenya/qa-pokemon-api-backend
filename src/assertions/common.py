from assertions.utils.allure import step
from assertions.utils.utils import extract_id_from_url
from hamcrest import assert_that, equal_to


@step
def verify_id(entity, expected_id):
    assert_that(entity["id"], equal_to(expected_id))


@step
def verify_name(entity, expected_entity_name):
    assert_that(entity["name"], equal_to(expected_entity_name))


@step
def verify_quantity(list_of_entities, expected_list_of_entities):
    assert_that(len(list_of_entities), equal_to(len(expected_list_of_entities)))


@step
def verify_ordering_by_id(list_of_entities, expected_ordered_list_of_entities_by_id):
    for index, expected_entity in enumerate(expected_ordered_list_of_entities_by_id):
        actual_pokemon_name = list_of_entities[index]["name"]
        assert_that(actual_pokemon_name, equal_to(expected_entity.name))


@step
def verify_named_resource_url(
    entity, expected_entity_id, expected_entity_url_placeholder
):
    actual_entity_url = entity["url"]
    expected_entity_url = expected_entity_url_placeholder.format(
        id_or_name=expected_entity_id
    )
    assert_that(actual_entity_url, equal_to(expected_entity_url))


@step
def verify_named_resource(entity, expected_entity, expected_entity_url_placeholder):
    verify_name(entity, expected_entity.name)
    verify_named_resource_url(
        entity, expected_entity.id, expected_entity_url_placeholder
    )


@step
def verify_named_resources(
    entities_from_response: list[dict],
    expected_list_of_entities: list,
    expected_entity_url_placeholder: str,
):
    dict_of_entities_w_ids = {
        extract_id_from_url(entity["url"]): entity for entity in entities_from_response
    }

    for expected_entity in expected_list_of_entities:
        actual_entity = dict_of_entities_w_ids[expected_entity.id]
        verify_named_resource(
            actual_entity, expected_entity, expected_entity_url_placeholder
        )
