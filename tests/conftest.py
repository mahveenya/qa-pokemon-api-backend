from api_client import ApiClient
import pytest


@pytest.fixture(scope="session")
def client():
    client = ApiClient()
    yield client
    client.close()
