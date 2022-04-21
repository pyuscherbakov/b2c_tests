from hamcrest import *
from core.api.authorization.data import schema
from core.utils.api_client import test_api_url
from jsonschema import validate
from core.api.endpoints import AUTH
import settings
import allure


# TODO: Написать проверку на авторизацию с невалидным аккаунтом


class TestAuth:

    @allure.feature('Авторизация')
    @allure.title('Получить токен')
    def test_get_token(self, test_api_url):
        user = settings.default_user
        response = test_api_url.post(AUTH, verify=False, json={"email": user[0], "password": user[1]})
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))
        with allure.step("Токен получен"):
            assert_that(response.json()["data"]["token"], is_not(None))
        with allure.step("Проверить схему ответа"):
            validate(response.json(), schema)

