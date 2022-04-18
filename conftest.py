import pytest
import requests


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        return requests.get(url=url, params=params, headers=headers)

    def put(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        return requests.put(url=url, params=params, data=data, json=json, headers=headers)


@pytest.fixture
def test():
    return ApiClient(base_address="https://b2c.test.fast-system.ru")