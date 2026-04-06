from api.api_client import Client, CoreClient
from db.db_client import DB, DBClient
import pytest


@pytest.fixture(scope="session")
def client():
    core_client = CoreClient()
    client = Client(core_client)
    yield client
    core_client.close()


@pytest.fixture(scope="session")
def db():
    client = DBClient()
    db = DB(client)
    yield db
    client.close()
