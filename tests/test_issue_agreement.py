import pytest
from core.api.contracts.contracts import Contract
from core.api.agreements.agreements import Agreement
import allure


# TODO: Организовать получение токена в фикстуре

class Test:
    @pytest.mark.parametrize("product", ["ingos_kasko", "alfastrah_kasko"])
    @pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
    @allure.feature('Оформление договора')
    @allure.title(f'Оформить договор')
    def test_issue_agreement(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.issue_agreement()
        agreement.agreement_get_status()
        agreement.get_payment_url()
