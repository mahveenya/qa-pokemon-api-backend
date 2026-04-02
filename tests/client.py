import os

import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.base_url = BASE_URL

    def get(self, path, **kwargs):
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def close(self):
        self.session.close()
