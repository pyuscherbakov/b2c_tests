from core.utils import check
from core.api.authorization import get_token
from core.api.endpoints import PROFILE
from core.api.profile.data import schema
from jsonschema import validate
import allure


class TestProfile:

    @allure.feature('Профиль')
    @allure.title('Получить данные профиля')
    def test_validate_response_json_schema(self, test_api_url):
        token = get_token()
        response = test_api_url.get(PROFILE, verify=False, headers={'Authorization': f'Bearer {token}'})
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200
        with allure.step("Проверить схему ответа"):
            return validate(response.json(), schema)

