import pytest
from core.api.contracts.contracts import Contract
from core.api.agreements.agreements import Agreement
import allure


@pytest.mark.parametrize("product", ["ingos_kasko", "alfastrah_kasko"])
@pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
@allure.feature('Оформление договора')
class Test:
    def test_issue_agreement(self, product, franchise):
        contract = Contract()
        contract.create_contracts(franchise)
        contract.create_calculation(product)
        contract.get_calculation()            # Проверка успешности расчета
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.issue_agreement()
        agreement.agreement_get_status()


