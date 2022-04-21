import time
from core.api.endpoints import CONTRACTS
from core.utils.api_client import ApiClient
from core.api.contracts import data
from core.api.authorization import get_token
from jsonschema import validate
import settings
import allure
# TODO: реализовать ассерты через humcrest


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
        with allure.step("Полученное в ответе поле ID не пустое"):
            assert response["data"]["id"] is not None
        self.contract_id = response["data"]["id"]
        allure.attach(self.contract_id, 'Contract id', allure.attachment_type.TEXT)

    def get_contract_id(self):
        return self.contract_id

    @allure.step(f"Создать расчет")
    def create_calculation(self, product):
        data.body_create_calculation["products"][0]["id"] = product
        response = self.base_url.post(CONTRACTS.CALCULATE.format(self.contract_id), verify=False,
                                      headers={'Authorization': f'Bearer {self.token}'},
                                      json=data.body_create_calculation)
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 202, f"Ожидался статус код 202, получен {response.status_code}"
        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_create_calculation)

    @allure.step("Получить расчет")
    def get_calculation(self):
        response = self.base_url.get(CONTRACTS.CALCULATE.format(self.contract_id), verify=False,
                                     headers={'Authorization': f'Bearer {self.token}'})
        status = response.json()["products"][0]["status"]
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"
        with allure.step("Проверить статус расчета"):
            if status == "Executing" or status == "InQueue":
                time.sleep(5)
                with allure.step(f"Статус расчета {status}. Проверить расчет еще раз."):
                    self.get_calculation()
            else:
                assert status == "Success", f"Ожидался статус Success, получен {status} " \
                                            f"с ошибкой {response.json()['products'][0]['errors']}"
                with allure.step("Проверить схему ответа"):
                    validate(response.json(), data.schema_get_calculation)

    @allure.step("Получить контракт")
    def get_contract(self):
        response = self.base_url.get(CONTRACTS.GET_CALCULATE.format(self.contract_id), verify=False,
                                     headers={'Authorization': f'Bearer {self.token}'})
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"
        with allure.step("Проверить отправленный на создание контракт с полученным"):
            with allure.step("Проверить данные ТС"):
                for item in response.json()["data"]["vehicle"]:
                    assert data.body_create_contract["vehicle"][item] == response.json()["data"]["vehicle"][item], \
                        "Данные ТС отправленные при создании контракта отличаются с полученными данными"
            with allure.step("Проверить условия страхования"):
                for item in response.json()["data"]["terms"]:
                    assert data.body_create_contract["terms"][item] == response.json()["data"]["terms"][item], \
                        f"Условия отправленные при создании контракта отличаются с полученными условиями"

    @allure.step("Обновить контракт")
    def update_contract(self):
        response = self.base_url.put(CONTRACTS.UPDATE.format(self.contract_id), verify=False,
                                     headers={'Authorization': f'Bearer {self.token}'},
                                     json=data.body_with_update_contract)
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"
        with allure.step("Проверить отправленный на обновление контракт с полученным"):
            with allure.step("Проверить данные ТС"):
                for item in response.json()["data"]["vehicle"]:
                    assert data.body_with_update_contract["vehicle"][item] == response.json()["data"]["vehicle"][item],\
                        "Данные ТС отправленные при обновлении контракта отличаются с полученными данными"
            with allure.step("Проверить условия страхования"):
                for item in response.json()["data"]["terms"]:
                    assert data.body_with_update_contract["terms"][item] == response.json()["data"]["terms"][item], \
                        f"Условия отправленные при обновлении контракта отличаются с полученными условиями"

    @allure.step("Получить обновленный контракт")
    def get_updated_contract(self):
        response = self.base_url.get(CONTRACTS.GET_CALCULATE.format(self.contract_id), verify=False,
                                     headers={'Authorization': f'Bearer {self.token}'})
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"
        with allure.step("Проверить отправленный на обновление контракт с полученным"):
            with allure.step("Проверить данные ТС"):
                for item in response.json()["data"]["vehicle"]:
                    assert data.body_with_update_contract["vehicle"][item] == response.json()["data"]["vehicle"][item],\
                        "Данные ТС отправленные при обновлении контракта отличаются с полученными данными"
            with allure.step("Проверить условия страхования"):
                for item in response.json()["data"]["terms"]:
                    assert data.body_with_update_contract["terms"][item] == response.json()["data"]["terms"][item], \
                        f"Условия отправленные при обновлении контракта отличаются с полученными условиями"