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
            assert response.status_code == 200
        with allure.step("Токен получен"):
            assert response.json()["data"]["token"] is not None
        with allure.step("Проверить схему ответа"):
            validate(response.json(), schema)

