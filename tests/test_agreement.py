from core.api.agreements.agreements import Agreement
from core.api.contracts.contracts import Contract
import allure
import pytest


class TestContracts:
    @pytest.mark.parametrize("product", ["ingos_kasko", "alfastrah_kasko"])
    @pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
    @allure.feature('Договор')
    @allure.story('Получить договор')
    def test_issue_agreement(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.get_agreement("Draft1")

