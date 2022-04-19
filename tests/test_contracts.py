from core.api.authorization import get_token
from core.api.contracts.contracts import Contract
import allure
import pytest


class TestContracts:
    @pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
    @allure.feature('Контракт')
    @allure.title('Создать контракт')
    def test_create_agreements(self, franchise):
        contract = Contract()
        contract.create_contract(franchise)

