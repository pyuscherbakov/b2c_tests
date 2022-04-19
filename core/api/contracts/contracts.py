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
    def __init__(self, franchise):
        self.contract_id = None
        self.token = get_token()
        self.base_url = ApiClient(settings.base_url)
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

    @allure.step("Получить contract ID")
    def get_contract_id(self):
        return self.contract_id

    @allure.step("Создать расчет")
    def create_calculation(self, product):
        # headers = {'Authorization': f'Bearer {self.token}'}
        # url = settings.base_url + CONTRACTS.CALCULATE.format(self.contract_id)
        data.body_create_calculation["products"][0]["id"] = product
        # r = requests.post(url, verify=False, headers=headers, json=body_create_calculation)
        response = self.base_url.post(CONTRACTS.CALCULATE.format(self.contract_id), verify=False,
                                      headers={'Authorization': f'Bearer {self.token}'},
                                      json=data.body_create_calculation)
        with allure.step("Проверить статус код ответа (202)"):
            print(response.json())
            assert response.status_code == 202, f"Ожидался статус код 202, получен {response.status_code}"

        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_create_calculation)

    @allure.step("Получить расчет")
    def get_calculation(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        url = settings.base_url + CONTRACTS.CALCULATE.format(self.contract_id)
        r = requests.get(url, verify=False, headers=headers)
        status = r.json()["products"][0]["status"]
        if status == "Executing" or status == "InQueue":
            time.sleep(3)
            self.get_calculation()
