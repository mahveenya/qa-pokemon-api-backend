from http import HTTPStatus
import os

from hamcrest import assert_that, equal_to
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.base_url = BASE_URL

    def close(self):
        self.session.close()

    def get(
        self, path, expected_status=HTTPStatus.OK, jsonify=True, **kwargs
    ) -> dict | requests.Response:
        res = self.session.get(f"{self.base_url}{path}", **kwargs)
        assert_that(res.status_code, equal_to(expected_status))
        respose = res.json() if jsonify else res
        return respose
