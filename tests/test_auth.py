from hamcrest import *
from core.api.authorization.data import schema
from jsonschema import validate
from core.api.endpoints import AUTH
import settings
import allure
import requests


# TODO: Написать проверку на авторизацию с невалидным аккаунтом


class TestAuth:

    @allure.feature('Авторизация')
    @allure.title('Получить токен')
    def test_get_token(self):
        url = settings.base_url + AUTH
        user = settings.default_user
        r = requests.post(url, verify=False, json={"email": user[0], "password": user[1]})
        with allure.step("Проверить статус код ответа"):
            assert_that(r.status_code, equal_to(200))
        with allure.step("Токен получен"):
            assert_that(r.json()["data"]["token"], is_not(None))
        with allure.step("Проверить схему ответа"):
            validate(r.json(), schema)

