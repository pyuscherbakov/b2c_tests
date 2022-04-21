from core.api.contracts.contracts import Contract
import allure
import pytest


class TestContracts:
    @pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
    @allure.feature('Контракт')
    @allure.story('Получить контракт')
    def test_get_calculation(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.get_contract()

    @allure.feature('Контракт')
    @allure.story('Обновить контракт')
    def test_update_contract(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()

