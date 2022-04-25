import time
from hamcrest import *
from core.utils.api_client import ApiClient
from core.api.endpoints import AGREEMENTS
import core.api.contracts.data as data_contract
from core.api.agreements import data
import allure
from jsonschema import validate
from datetime import date
# TODO: Установить счетчик запросов


class Agreement:
    api = ApiClient()

    def __init__(self, contract_id, product):
        self.contract_id = contract_id
        self.product = product
        self.agreement_id = None
        self.payment_link = None

    @allure.step("Создать договор")
    def create_agreement(self):
        data.body_create_agreement["contract_id"] = self.contract_id
        data.body_create_agreement["product_id"] = self.product
        response = self.api.post(AGREEMENTS.CREATE,
                                 json=data.body_create_agreement)
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, is_in([200, 202]))
        response = response.json()
        time.sleep(10)
        if response.get("status"):
            with allure.step(f"Договор не создан. Отправить повторный запрос."):
                with allure.step(f"Проверить схему ответа при статусе {response['status']}"):
                    validate(response, data.schema_with_not_success)
                with allure.step(f"Договор не имеет статус 'error'"):
                    assert_that(response["status"], is_not(equal_to("error")))
                time.sleep(10)
                self.create_agreement()
        else:
            self.agreement_id = response["id"]
            self.attach_agreement_data()
            with allure.step(f"Ответ содержит в себе ID договора"):
                assert_that(response["id"], is_not(None))
            with allure.step(f"Проверить схему успешного ответа"):
                validate(response, data.schema_with_success)

    @allure.step("Оформить договор")
    def issue_agreement(self):
        response = self.api.post(AGREEMENTS.ISSUE.format(self.agreement_id),
                                 json=data.body_create_agreement)
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, is_in([200, 202]))
        with allure.step(f"Договор встал в очередь на оформление"):
            assert_that(response.json()["status"], equal_to("InQueue"))
        with allure.step(f"Проверить схему ответа"):
            validate(response.json(), data.schema_issue_agreement)

    @allure.step("Проверить статус оформления договора")
    def agreement_get_status(self):
        response = self.api.get(AGREEMENTS.TASK.format(self.agreement_id))
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))
        with allure.step("Статус выполнения операции получен"):
            assert_that(response.json().get("status"))
        status = response.json()["status"]
        if status == "Executing" or status == "InQueue":
            time.sleep(10)
            with allure.step(f"Повторно проверить статус договора. Текущий статус договора {status}."):
                self.agreement_get_status()
        else:
            if self.product == "alfastrah_kasko" and \
                    response.json()['errors'] == ['Неопознанная ошибка в ответе страховой компании']:
                with allure.step(f"Повторно отправить запрос на оформление договора."
                                 f"Обнаружена ошибка {response.json()['errors']}"):
                    self.issue_agreement()
                    self.agreement_get_status()
            else:
                with allure.step(f"Договор не содержит ошибок"):
                    assert_that(status, is_not(equal_to("Error")))
                with allure.step(f"Договор успешно оформлен"):
                    assert_that(status, equal_to("Success"))
                with allure.step(f"Проверить схему ответа"):
                    validate(response.json(), data.schema_get_status)

    @allure.step("Получить ссылку на оплату")
    def get_payment_url(self):
        response = self.api.post(AGREEMENTS.ISSUE.format(self.agreement_id),
                                 json=data.body_create_agreement)
        assert_that(response.json().get("payment_url"))
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, is_in([200, 202]))
        assert_that(response.json().get("payment_url"))
        if response.json().get("payment_url"):
            self.payment_link = response.json()['payment_url']
            res = f"Контракт: {self.contract_id}\nДоговор: {self.agreement_id}\n" \
                  f"Ссылка на оплату: {response.json()['payment_url']}\n" \
                  f"Ссылка действительна до: {response.json()['payment_url_lifetime']}"
            allure.attach(res, 'Ссылка на оплату', allure.attachment_type.TEXT)

    @allure.step("Получить договор")
    def get_agreement(self, agreement_status):
        response = self.api.get(AGREEMENTS.GET.format(self.agreement_id))
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))
        with allure.step("Проверить дату оформления договора"):
            assert_that(response.json()["agreement_date"], equal_to(str(date.today())))
        with allure.step("Условия полученного договора совпадают с условями в отправленном контракте при его создании"):
            for item in response.json()["terms"]["kasko"]:
                assert_that(data_contract.body_create_contract["terms"]["kasko"][item],
                            equal_to(response.json()["terms"]["kasko"][item]))
        with allure.step("Договор не имеет сообщений об ошибке"):
            assert_that(response.json()["errors"], is_(empty()))
        with allure.step("Проверить статус договора"):
            assert_that(response.json()["status"], equal_to(agreement_status))
        with allure.step("Проверить схему ответа"):
            if agreement_status == "AwaitingPayment" and "payment_url" not in data.schema_get_agreement["properties"]:
                data.schema_get_agreement["required"].append("payment_url")
                data.schema_get_agreement["properties"]["payment_url"] = {"type": "string"}
            validate(response.json(), data.schema_get_agreement)

    @allure.step("Получить документы по договору")
    def get_documents(self):
        response = self.api.get(AGREEMENTS.DOCUMENTS.format(self.agreement_id))
        with allure.step("Проверить статус код ответа"):
            assert_that(response.status_code, equal_to(200))
        with allure.step("Проверить полученные документы"):
            for document in response.json():
                with allure.step(f"Статус документа: {document['name']}– Success"):
                    assert_that(document["success"], equal_to(True))
        with allure.step("Проверить схему ответа"):
            validate(response.json(), data.schema_documents)

    def attach_agreement_data(self):
        res = f"Контракт: {self.contract_id}\n" \
              f"Договор: {self.agreement_id}\n" \
              f"Ссылка на оплату: {self.payment_link}"
        allure.attach(res, 'Данные', allure.attachment_type.TEXT)
