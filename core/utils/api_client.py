import requests
import allure
import json as m_json
from core.api.authorization import get_token
from tests.b2c.settings import base_url
from loguru import logger


class ApiClient:
    def __init__(self):
        self.base_address = base_url
        self.token = get_token()

    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'Отправить POST запрос: {url}'):
            r = requests.post(
                url=url,
                params=params,
                data=data,
                json=json,
                headers=self._get_headers(headers),
                verify=False,
            )
            logger.info(f"Отправить POST запрос.\n"
                        f"URL: {url}\n"
                        f"Тело запроса: {json}\n"
                        f"Тело ответа: {r.json()}\n")
            allure.attach(m_json.dumps(json, indent=4), 'Тело запроса', allure.attachment_type.JSON)
            allure.attach(m_json.dumps(r.json(), indent=4), 'Тело ответа', allure.attachment_type.JSON)
            return r

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'Отправить GET запрос: {url}'):
            r = requests.get(
                url=url,
                params=params,
                headers=self._get_headers(headers),
                verify=False,
            )
            logger.info(f"Отправить GET запрос.\n"
                        f"URL: {url}\n"
                        f"Тело ответа: {r.json()}\n")
            allure.attach(m_json.dumps(r.json(), indent=4), 'Тело ответа', allure.attachment_type.JSON)
            return r

    def put(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'Отправить PUT запрос: {url}'):
            r = requests.put(
                url=url,
                params=params,
                data=data,
                json=json,
                headers=self._get_headers(headers),
                verify=False,
            )
            logger.info(f"Отправить PUT запрос.\n"
                        f"URL: {url}\n"
                        f"Тело запроса: {json}\n"
                        f"Тело ответа: {r.json()}\n")
            allure.attach(m_json.dumps(json, indent=4), 'Тело запроса', allure.attachment_type.JSON)
            allure.attach(m_json.dumps(r.json(), indent=4), 'Тело ответа', allure.attachment_type.JSON)
            return r

    def _get_headers(self, headers):
        headers = headers if headers else dict()
        return {'Authorization': f'Bearer {self.token}', **headers}

