import time
import requests
from core.utils.api_client import ApiClient
from core.api.endpoints import AGREEMENTS
from core.api.agreements.data import body_create_agreement
from core.api.authorization import get_token
import settings
import allure
from jsonschema import validate
from core.api.agreements import data


class Agreement:
    base_url = ApiClient(settings.base_url)

    def __init__(self, contract_id, product):
        self.contract_id = contract_id
        self.product = product
        self.token = get_token()
        self.agreement_id = None

    @allure.step("Создать договор")
    def create_agreement(self):
        body_create_agreement["contract_id"] = self.contract_id
        body_create_agreement["product_id"] = self.product
        response = self.base_url.post(AGREEMENTS.CREATE, verify=False,
                                      headers={'Authorization': f'Bearer {self.token}'},
                                      json=body_create_agreement)
        with allure.step("Проверить статус код ответа"):
            assert response.status_code in [200, 202]
        response = response.json()
        if response.get("status"):
            with allure.step(f"Проверить схему ответа при статусе {response['status']}"):
                validate(response, data.schema_with_not_success)
            time.sleep(10)
            # TODO: убрать шаги повторного вызова метода создания договора из отчетов
            self.create_agreement()
        else:
            self.agreement_id = response["id"]
            with allure.step(f"Проверить схему успешного ответа"):
                validate(response, data.schema_with_success)

    @allure.step("Оформить договор")
    def issue_agreement(self):
        response = self.base_url.post(AGREEMENTS.ISSUE.format(self.agreement_id), verify=False,
                                      headers={'Authorization': f'Bearer {self.token}'},
                                      json=body_create_agreement)
        with allure.step("Проверить статус код ответа"):
            assert response.status_code in [200, 202], f"Ожидался статус код 200 или 202, " \
                                                       f"получен {response.status_code}"
        response = response.json()
        with allure.step(f"Проверить схему ответа"):
            validate(response, data.schema_issue_agreement)

    @allure.step("Проверить статус оформления договора")
    def agreement_get_status(self):
        response = self.base_url.get(AGREEMENTS.TASK.format(self.agreement_id), verify=False,
                                     headers={'Authorization': f'Bearer {self.token}'})
        status = response.json()["status"]
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200
        if status == "Executing" or status == "InQueue":
            time.sleep(11)
            with allure.step(f"Повторно проверить статус договора. Статус договора {status}."):
                self.agreement_get_status()
        else:
            if self.product == "alfastrah_kasko" and \
                    response.json()['errors'] == ['Неопознанная ошибка в ответе страховой компании']:
                with allure.step(f"Повторно отправить запрос на оформление договора."
                                 f"Обнаружена ошибка {response.json()['errors']}"):
                    self.issue_agreement()
            else:
                with allure.step(f"Договор не содержит ошибок"):
                    assert status != "Error", f"Получена ошибка {response.json()['errors']}"
                with allure.step(f"Договор успешно оформлен"):
                    assert status == "Success" and status != "Error", f"Договор не оформлен. Статус договора: {status}"

    @allure.step("Получить ссылку на оплату")
    def get_payment_url(self):
        url = settings.base_url + AGREEMENTS.ISSUE.format(self.agreement_id)
        headers = {'Authorization': f'Bearer {self.token}'}
        r = requests.post(url, verify=False, headers=headers)
        assert r.json().get("payment_url"), "Ссылка на оплату не получена"
        if r.json().get("payment_url"):
            print(f"Контракт: {self.contract_id}\nДоговор: {self.agreement_id}")
            print(f"Ссылка на оплату: {r.json()['payment_url']}")
            print(f"Ссылка действительна до: {r.json()['payment_url_lifetime']}")
        else:
            print(r.json())
