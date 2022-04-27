from core.api.contracts.contracts import Contract
import allure
import pytest


@pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
class TestContracts:
    @allure.feature('Контракт')
    @allure.story('Создать контракт')
    @allure.title('Создать контракт')
    def test_create_contract(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()

    @pytest.mark.parametrize("product", [
        # "ingos_kasko",
        "alfastrah_kasko"])
    @allure.feature('Контракт')
    @allure.story('Создать расчет')
    @allure.title('Создать расчет')
    def test_create_calculation(self, franchise, product):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)

    @allure.feature('Контракт')
    @allure.story('Получить контракт')
    @allure.title('Получить контракт')
    def test_get_contract(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.get_contract()

    @pytest.mark.parametrize("product", [
        # "ingos_kasko",
        "alfastrah_kasko"])
    @allure.feature('Контракт')
    @allure.story('Получить расчет')
    @allure.title('Получить расчет')
    def test_get_calculation(self, franchise, product):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()

    @allure.feature('Контракт')
    @allure.story('Обновить контракт')
    @allure.title('Обновить контракт')
    def test_update_contract(self, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.update_contract("purchase_date")
        contract.get_updated_contract()
