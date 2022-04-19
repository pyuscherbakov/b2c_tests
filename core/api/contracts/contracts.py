import time
import requests
from core.api.endpoints import CONTRACTS
from core.utils.api_client import ApiClient
from core.api.contracts import data
from core.api.authorization import get_token
from jsonschema import validate
import settings
import allure


class Contract:
    base_url = ApiClient(settings.base_url)

    def __init__(self, franchise):
        self.contract_id = None
        self.token = get_token()
        self.franchise = franchise

    @allure.step("Создать контракт")
    def create_contract(self):
        data.body_create_contract["terms"]["kasko"]["franchise"] = self.franchise
        response = self.base_url.post(CONTRACTS.CREATE, verify=False,
                                      headers={'Authorization': f'Bearer {self.token}'},
                                      json=data.body_create_contract)
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200
        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_create_contract)
        response = response.json()
        self.contract_id = response["data"]["id"]

    def get_contract_id(self):
        return self.contract_id

    @allure.step("Создать расчет")
    def create_calculation(self, product):
        data.body_create_calculation["products"][0]["id"] = product
        response = self.base_url.post(CONTRACTS.CALCULATE.format(self.contract_id), verify=False,
                                      headers={'Authorization': f'Bearer {self.token}'},
                                      json=data.body_create_calculation)
        with allure.step("Проверить статус код ответа (202)"):
            assert response.status_code == 202, f"Ожидался статус код 202, получен {response.status_code}"
        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_create_calculation)

    @allure.step("Получить расчет")
    def get_calculation(self):
        # headers = {'Authorization': f'Bearer {self.token}'}
        # url = settings.base_url + CONTRACTS.CALCULATE.format(self.contract_id)
        # r = requests.get(url, verify=False, headers=headers)
        response = self.base_url.get(CONTRACTS.CALCULATE.format(self.contract_id), verify=False,
                                     headers={'Authorization': f'Bearer {self.token}'})
        status = response.json()["products"][0]["status"]
        with allure.step("Проверить статус расчета"):
            if status == "Executing" or status == "InQueue":
                time.sleep(5)
                with allure.step(f"Статус расчета {status}. Проверить еще раз."):
                    self.get_calculation()
            else:
                assert status == "Success", f"Ожидался статус Success, получен {status} " \
                                            f"с ошибкой {response.json()['products'][0]['errors']}"
