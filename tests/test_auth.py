from core.api.authorization.data import schema
from jsonschema import validate
from core.api.endpoints import AUTH
import settings
import allure

"""
Написать проверку на авторизацию с невалидным аккаунтом
"""


class TestAuth:

    @allure.feature('Авторизация')
    @allure.title('Получить токен')
    def test_get_token(self, test_api_url):
        user = settings.default_user
        response = test_api_url.post(AUTH, verify=False, json={"email": user[0], "password": user[1]})
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200
        with allure.step("Ответ содержит токен"):
            assert "token" in str(response.content)
        with allure.step("Проверить схему ответа"):
            return validate(response.json(), schema)