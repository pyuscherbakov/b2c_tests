import pytest
from core.api.contracts.contracts import Contract
from core.api.agreements.agreements import Agreement
import allure


@allure.feature('Договор')
@allure.story('Оформить договор')
class TestsIssueAgreement:
    @pytest.mark.parametrize("product", [
        "ingos_kasko",
        "alfastrah_kasko",
    ])
    @pytest.mark.parametrize("franchise", [
        "Нет",
        "Безусловная 15 тыс."
    ])
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
        res = f"Контракт: {contract.contract_id}\n" \
              f"Договор: {agreement.agreement_id}\n" \
              f"Ссылка на оплату: {agreement.payment_link}"
        allure.attach(res, 'Ссылка на оплату', allure.attachment_type.TEXT)

