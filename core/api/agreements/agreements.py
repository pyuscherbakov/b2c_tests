import time
import requests

from core.api.endpoints import AGREEMENTS
from core.api.agreements.data import body_create_agreement
from core.api.authorization import get_token
import settings


class Agreement:
    def __init__(self, contract_id, product):
        self.contract_id = contract_id
        self.product = product
        self.token = get_token()
        self.agreement_id = None

    def create_agreement(self):
        url = settings.base_url + AGREEMENTS.CREATE
        headers = {'Authorization': f'Bearer {self.token}'}
        body_create_agreement["contract_id"] = self.contract_id
        body_create_agreement["product_id"] = self.product
        r = requests.post(url, verify=False, headers=headers, json=body_create_agreement)
        response = r.json()
        if response.get("status"):
            time.sleep(5)
            self.create_agreement()
        else:
            print(response)
            self.agreement_id = response['id']

    def issue_agreement(self):
        url = settings.base_url + AGREEMENTS.ISSUE.format(self.agreement_id)
        headers = {'Authorization': f'Bearer {self.token}'}
        r = requests.post(url, verify=False, headers=headers)

    def agreement_get_status(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        url = settings.base_url + AGREEMENTS.TASK.format(self.agreement_id)
        r = requests.get(url, verify=False, headers=headers)
        status = r.json()["status"]
        if status == "Executing" or status == "InQueue":
            time.sleep(10)
            self.agreement_get_status()
        else:
            if self.product == "alfastrah_kasko" and \
                    r.json()['errors'] == ['Неопознанная ошибка в ответе страховой компании']:
                self.issue_agreement()
            else:
                assert status != "Error", f"Ошибка при оформлении договора{r.json()['errors']}"
                assert status == "Success", f"Договор не оформлен. {status}"
                self.get_payment_url()

    def get_payment_url(self):
        url = settings.base_url + AGREEMENTS.ISSUE.format(self.agreement_id)
        headers = {'Authorization': f'Bearer {self.token}'}
        r = requests.post(url, verify=False, headers=headers)
        assert r.json().get("payment_url"), "Ссылка на оплату не получена"
        if r.json().get("payment_url"):
            print(f"Контракт: {self.contract_id}\nДоговор: {self.agreement_id}")
            print(f"Ссылка на оплату: {r.json()['payment_url']}")
            print(f"Ссылка действительна до: {r.json()['payment_url_lifetime']}")
