from jsonschema import validate
import allure


@allure.step("Проверка схемы ответа")
def check_validate_schema(response, schema):
    with allure.step("Валидация схемы ответа"):
        return validate(response.json(), schema)

