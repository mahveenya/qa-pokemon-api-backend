from client import Client
import pytest


@pytest.fixture(scope="session")
def client():
    client = Client()
    yield client
    client.close()
