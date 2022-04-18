import time
import requests
from core.api.endpoints import CONTRACTS
from core.api.contracts.data import body_create_contract, body_create_calculation
from core.api.authorization import get_token
import settings


class Contract:
    def __init__(self):
        self.contract_id = None
        self.token = get_token()

    def create_contracts(self, franchise):
        url = settings.base_url + CONTRACTS.CREATE
        headers = {'Authorization': f'Bearer {self.token}'}
        body_create_contract["terms"]["kasko"]["franchise"] = franchise
        r = requests.post(url, verify=False, headers=headers, json=body_create_contract)
        response = r.json()
        self.contract_id = response["data"]["id"]

    def get_contract_id(self):
        return self.contract_id

    def create_calculation(self, product):
        headers = {'Authorization': f'Bearer {self.token}'}
        url = settings.base_url + CONTRACTS.CALCULATE.format(self.contract_id)
        body_create_calculation["products"][0]["id"] = product
        r = requests.post(url, verify=False, headers=headers, json=body_create_calculation)

    def get_calculation(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        url = settings.base_url + CONTRACTS.CALCULATE.format(self.contract_id)
        r = requests.get(url, verify=False, headers=headers)
        status = r.json()["products"][0]["status"]
        if status == "Executing" or status == "InQueue":
            time.sleep(3)
            self.get_calculation()
