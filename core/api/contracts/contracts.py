import time
from hamcrest import *
from core.api.endpoints import CONTRACTS
from core.utils.api_client import ApiClient
from core.api.contracts import data
from jsonschema import validate
import allure
import datetime
from loguru import logger
# TODO: добавить в отчет сумму премии


class Contract:
    api = ApiClient()

    def __init__(self, franchise):
        self.contract_id = None
        self.franchise = franchise
        self.cnt_get_calc = 0
        self.product_id = None

    @allure.step("Создать контракт")
    @logger.catch()
    def create_contract(self):
        logger.info(f"Вызван метод создания контракта")
        data.body_create_contract["terms"]["kasko"]["franchise"] = self.franchise
        response = self.api.post(CONTRACTS.CREATE, json=data.body_create_contract)

        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))

        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_create_contract)

        response = response.json()

        self.contract_id = response["data"]["id"]

        logger.info(f"Создан контракт {self.contract_id}")
        allure.attach(self.contract_id, 'Contract id', allure.attachment_type.TEXT)

    def get_contract_id(self):
        return self.contract_id

    @allure.step(f"Создать расчет")
    @logger.catch()
    def create_calculation(self, product):
        data.body_create_calculation["products"][0]["id"] = product
        self.product_id = product
        logger.info(f"Контракт отправлен на расчет. Contract ID: {self.contract_id}")
        response = self.api.post(CONTRACTS.CALCULATE.format(self.contract_id), json=data.body_create_calculation)

        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, is_in([200, 202]))

        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_create_calculation)

    @allure.step("Получить расчет")
    @logger.catch()
    def get_calculation(self):
        max_returns = 20
        logger.info(f"Получить расчет. Попытка: {self.cnt_get_calc}. Contract ID: {self.contract_id}")
        response = self.api.get(CONTRACTS.CALCULATE.format(self.contract_id))
        status = response.json()["products"][0]["status"]

        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))

        with allure.step("Проверить статус расчета"):
            if self.cnt_get_calc < max_returns:
                self.cnt_get_calc += 1
                if status == "Executing" or status == "InQueue":
                    time.sleep(5)

                    with allure.step(f"Статус расчета {status}. Проверить расчет еще раз."):
                        logger.info(f"Полученный статус расчета: {status}. Contract ID: {self.contract_id}")
                        self.get_calculation()
                else:
                    assert_that(status, equal_to("Success"), f"Получена ошибка: "
                                                             f"{response.json()['products'][0]['errors']}")

                    with allure.step("Проверить схему ответа"):
                        validate(response.json(), data.schema_get_calculation)

                    logger.info(f"Расчет получен. Премия: {response.json()['products'][0]['premium']}. "
                                f"Продукт: {self.product_id}. Contract ID: {self.contract_id}")
            else:
                if self.cnt_get_calc >= max_returns:
                    logger.error(f"Выполнено слишком много попыток получить расчет. Contract ID: {self.contract_id}")

                assert_that(self.cnt_get_calc, is_not(equal_to(max_returns)), "Выполнено слишком много попыток "
                                                                              "получить расчет")

    @allure.step("Получить контракт")
    @logger.catch()
    def get_contract(self):
        logger.info(f"Получить контракт. Contract ID: {self.contract_id}")
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
        logger.info(f"Контракт получен. Contract ID: {self.contract_id}")

    @allure.step("Обновить контракт")
    @logger.catch()
    def update_contract(self, updated_parameter):
        """
        :param updated_parameter: параметр, который требуется изменить в обновляемом договоре
        Доступные параметры:
        drivers
        purchase_date
        """
        if updated_parameter == "purchase_date":
            data.body_with_update_contract["terms"]["kasko"]["purchase_date"] = \
                str(datetime.date.today() - datetime.timedelta(days=5))
        elif updated_parameter == "drivers":
            data.body_with_update_contract["drivers"][0]["last_name"] = "Климов"

        logger.info(f"Обновить контракт. Обновляемый параметр: {updated_parameter}. Contract ID: {self.contract_id}")
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

        logger.info(f"Контракт обновлён. Contract ID: {self.contract_id}")

    @allure.step("Получить обновленный контракт")
    @logger.catch()
    def get_updated_contract(self):
        logger.info(f"Получить обновленный контракт. Contract ID: {self.contract_id}")
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

        logger.info(f"Обновленный контракт получен. Contract ID: {self.contract_id}")
