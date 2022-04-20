from jsonschema import validate
from core.api.endpoints import AUTH
from core.api.authorization.data import schema
from core.utils.api_client import *
import settings
import allure


class Token:
    base_url = ApiClient(settings.base_url)

    @staticmethod
    @allure.step("Получить токен")
    def get_token():
        user = settings.default_user
        response = base_url.post(AUTH, verify=False, json={"email": user[0], "password": user[1]})
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200
        with allure.step("Проверить схему ответа"):
            validate(response.json(), schema)
        return response.json()["data"]["token"]

