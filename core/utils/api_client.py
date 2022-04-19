import pytest
import requests
import allure
import json as m_json


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, json=None, headers=None, verify=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'Отправить POST запрос: {url}'):
            r = requests.post(url=url, params=params, data=data, json=json, headers=headers, verify=verify)
            allure.attach(m_json.dumps(json), 'Тело запроса', allure.attachment_type.JSON)
            allure.attach(r.text, 'Тело ответа', allure.attachment_type.JSON)
            return r

    def get(self, path="/", params=None, headers=None, verify=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'Отправить GET запрос: {url}'):
            r = requests.get(url=url, params=params, headers=headers, verify=verify)
            allure.attach(r.text, 'Тело ответа', allure.attachment_type.JSON)
            return r

    def put(self, path="/", params=None, data=None, json=None, headers=None, verify=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'Отправить PUT запрос: {url}'):
            r = requests.put(url=url, params=params, data=data, json=json, headers=headers, verify=verify)
            allure.attach(m_json.dumps(json), 'Тело запроса', allure.attachment_type.JSON)
            allure.attach(r.text, 'Тело ответа', allure.attachment_type.JSON)
            return r


@pytest.fixture
@allure.title("Получить URL")
def test_api_url():
    return ApiClient(base_address="https://b2c.test.fast-system.ru")
