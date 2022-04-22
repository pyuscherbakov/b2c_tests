import time
from hamcrest import *
from core.api.endpoints import CONTRACTS
from core.utils.api_client import ApiClient
from core.api.contracts import data
from jsonschema import validate
import allure


class Contract:
    api = ApiClient()

    def __init__(self, franchise):
        self.contract_id = None
        self.franchise = franchise

    @allure.step("Создать контракт")
    def create_contract(self):
        data.body_create_contract["terms"]["kasko"]["franchise"] = self.franchise
        response = self.api.post(CONTRACTS.CREATE, json=data.body_create_contract)
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))
        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_create_contract)
        response = response.json()
        with allure.step("Полученное в ответе поле ID не пустое"):
            assert_that(response["data"]["id"], is_not(None))
        self.contract_id = response["data"]["id"]
        allure.attach(self.contract_id, 'Contract id', allure.attachment_type.TEXT)

    def get_contract_id(self):
        return self.contract_id

    @allure.step(f"Создать расчет")
    def create_calculation(self, product):
        data.body_create_calculation["products"][0]["id"] = product
        response = self.api.post(CONTRACTS.CALCULATE.format(self.contract_id), json=data.body_create_calculation)
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, is_in([200, 202]))
        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_create_calculation)

    @allure.step("Получить расчет")
    def get_calculation(self):
        response = self.api.get(CONTRACTS.CALCULATE.format(self.contract_id))
        status = response.json()["products"][0]["status"]
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))
        with allure.step("Проверить статус расчета"):
            if status == "Executing" or status == "InQueue":
                time.sleep(5)
                with allure.step(f"Статус расчета {status}. Проверить расчет еще раз."):
                    self.get_calculation()
            else:
                assert_that(status, equal_to("Success"), f"Получена ошибка: {response.json()['products'][0]['errors']}")
                with allure.step("Проверить схему ответа"):
                    validate(response.json(), data.schema_get_calculation)

    @allure.step("Получить контракт")
    def get_contract(self):
        response = self.api.get(CONTRACTS.GET_CALCULATE.format(self.contract_id))
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))
        with allure.step("Проверить отправленный на создание контракт с полученным"):
            with allure.step("Проверить данные ТС"):
                for item in response.json()["data"]["vehicle"]:
                    assert_that(data.body_create_contract["vehicle"][item],
                                equal_to(response.json()["data"]["vehicle"][item]))
            with allure.step("Проверить условия страхования"):
                for item in response.json()["data"]["terms"]:
                    assert_that(data.body_create_contract["terms"][item],
                                equal_to(response.json()["data"]["terms"][item]))

    @allure.step("Обновить контракт")
    def update_contract(self):
        response = self.api.put(CONTRACTS.UPDATE.format(self.contract_id), json=data.body_with_update_contract)

        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))

        with allure.step("Проверить отправленный на обновление контракт с полученным"):
            with allure.step("Проверить данные ТС"):
                for item in response.json()["data"]["vehicle"]:
                    assert_that(data.body_with_update_contract["vehicle"][item],
                                equal_to(response.json()["data"]["vehicle"][item]))

            with allure.step("Проверить условия страхования"):
                for item in response.json()["data"]["terms"]:
                    assert_that(data.body_with_update_contract["terms"][item],
                                equal_to(response.json()["data"]["terms"][item]))

    @allure.step("Получить обновленный контракт")
    def get_updated_contract(self):
        response = self.api.get(CONTRACTS.GET_CALCULATE.format(self.contract_id))
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))

        with allure.step("Проверить отправленный на обновление контракт с полученным"):
            with allure.step("Проверить данные ТС"):
                for item in response.json()["data"]["vehicle"]:
                    assert_that(data.body_with_update_contract["vehicle"][item],
                                equal_to(response.json()["data"]["vehicle"][item]))

            with allure.step("Проверить условия страхования"):
                for item in response.json()["data"]["terms"]:
                    assert_that(data.body_with_update_contract["terms"][item],
                                equal_to(response.json()["data"]["terms"][item]))
