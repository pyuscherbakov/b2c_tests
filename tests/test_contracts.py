from core.api.authorization import get_token
from core.api.contracts.contracts import Contract
import allure
import pytest


class TestContracts:
    @pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
    @allure.feature('Контракт')
    @allure.title('Создать контракт')
    def test_create_agreements(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()

    @pytest.mark.parametrize("product", ["ingos_kasko", "alfastrah_kasko"])
    @pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
    @allure.feature('Контракт')
    @allure.title('Создать расчет')
    def test_create_calculation(self, franchise, product):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)


