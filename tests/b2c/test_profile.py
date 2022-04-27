from core.utils.api_client import ApiClient
from core.api.endpoints import PROFILE
from core.api.profile.data import schema
from jsonschema import validate
from hamcrest import *
import allure


class TestProfile:

    @allure.feature('Профиль')
    @allure.title('Получить данные профиля')
    def test_validate_response_json_schema(self):
        response = ApiClient().get(PROFILE)
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))
        with allure.step("Проверить схему ответа"):
            validate(response.json(), schema)

