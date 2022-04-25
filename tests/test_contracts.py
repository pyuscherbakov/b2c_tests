from core.api.contracts.contracts import Contract
import allure
import pytest


# TODO: прописать проверки остальных методов
@pytest.mark.parametrize("product", ["ingos_kasko", "alfastrah_kasko"])
@pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
class TestContracts:
    @allure.feature('Контракт')
    @allure.story('Создать контракт')
    def test_get_calculation(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()

    @allure.feature('Контракт')
    @allure.story('Создать расчет')
    def test_get_calculation(self, franchise, product):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)

    @allure.feature('Контракт')
    @allure.story('Получить контракт')
    def test_get_calculation(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.get_contract()

    @allure.feature('Контракт')
    @allure.story('Получить расчет')
    def test_get_calculation(self, franchise, product):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()

    @allure.feature('Контракт')
    @allure.story('Обновить контракт')
    def test_update_contract(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.update_contract()
        contract.get_updated_contract()
