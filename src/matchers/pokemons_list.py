from hamcrest import assert_that, equal_to
from src.db.db_client import db


def _verify_count(res):
    expected_count = db.pokemon.count_all_entries()
    assert_that(res["count"], equal_to(expected_count))


def _verify_results_count(res, expected_results_quantity):
    assert_that(len(res["results"]), equal_to(expected_results_quantity))


def verify_pokemon_quantity(res, expected_quantity):
    _verify_count(res)
    _verify_results_count(res, expected_quantity)
