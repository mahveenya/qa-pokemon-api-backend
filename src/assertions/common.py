from assertions.utils.allure import step
from assertions.utils.utils import extract_id_from_url
from hamcrest import assert_that, equal_to


@step
def verify_entity_name(entity, expected_entity_name):
    assert_that(entity["name"], equal_to(expected_entity_name))


@step
def _verify_entity_url(entity, expected_entity_id, expected_entity_url_placeholder):
    actual_entity_url = entity["url"]
    expected_entity_url = expected_entity_url_placeholder.format(
        id_or_name=expected_entity_id
    )
    assert_that(actual_entity_url, equal_to(expected_entity_url))


@step
def _verify_named_resource(entity, expected_entity, expected_entity_url_placeholder):
    verify_entity_name(entity, expected_entity.name)
    _verify_entity_url(entity, expected_entity.id, expected_entity_url_placeholder)


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
        _verify_named_resource(
            actual_entity, expected_entity, expected_entity_url_placeholder
        )
