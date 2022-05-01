from hamcrest import *
from core.api.authorization.data import *
from jsonschema import validate
from core.api.endpoints import AUTH
from tests.b2c import settings
import allure
import requests
from loguru import logger


class TestAuth:
    @allure.feature('Авторизация')
    @allure.story('Получить токен')
    @allure.title('Получить токен')
    def test_get_token_with_valid_account(self):
        url = settings.base_url + AUTH
        user = settings.default_user
        r = requests.post(url, verify=False, json={"email": user[0], "password": user[1]})
        logger.info(f"Отправить POST запрос на авторизацию. Аккаунт: {user[0]}:{user[1]}. Тело ответа: {r.json()}")
        with allure.step("Проверить статус код ответа"):
            assert_that(r.status_code, equal_to(200))
        with allure.step("Токен получен"):
            assert_that(r.json()["data"]["token"], is_not(None))
            logger.info(f"Токен получен. Аккаунт: {user[0]}:{user[1]}")
        with allure.step("Проверить схему ответа"):
            validate(r.json(), schema_with_success_auth)

    @allure.feature('Авторизация')
    @allure.story('Получить токен')
    @allure.title('Получить токен с невалидным аккаунтом')
    def test_get_token_with_invalid_account(self):
        url = settings.base_url + AUTH
        user = ("invalid@mail.ru", "wrong_password")
        r = requests.post(url, verify=False, json={"email": user[0], "password": user[1]})
        logger.info(f"Отправить POST запрос на авторизацию. Аккаунт: {user[0]}:{user[1]}. Тело ответа: {r.json()}")
        with allure.step("Проверить статус код ответа"):
            assert_that(r.status_code, equal_to(400))
        with allure.step("Токен не получен"):
            logger.info(f"Токен не получен. Аккаунт: {user[0]}:{user[1]}")
            assert_that(r.json(), is_not(has_key("data")))
        with allure.step("Проверить схему ответа"):
            validate(r.json(), schema_with_not_success_auth)

    def test_1(self):
        pass

    def test_2(self):
        pass


