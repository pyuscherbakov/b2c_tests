from core.api.agreements.agreements import Agreement
from core.api.contracts.contracts import Contract
import allure
import pytest
# TODO: прописать проверки остальных методов


@pytest.mark.parametrize("product", ["ingos_kasko", "alfastrah_kasko"])
@pytest.mark.parametrize("franchise", ["Нет", "Безусловная 15 тыс."])
class TestContracts:
    @allure.feature('Договор')
    # TODO: реализовать получение договора в других статусах (Issued)
    @allure.story('Получить договор')
    @allure.title('Получить договор со статусом Draft')
    def test_get_agreement_with_status_draft(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.get_agreement("Draft")

    @allure.feature('Договор')
    @allure.story('Получить договор')
    @allure.title('Получить договор со статусом AwaitingPayment')
    def test_get_agreement_with_status_awaiting_payment(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.issue_agreement()
        agreement.agreement_get_status()
        agreement.get_payment_url()
        agreement.get_agreement("AwaitingPayment")

    # @allure.feature('Договор')
    # @allure.story('Обновить договор')
    # def test_update_agreement(self):
    #     pass
    #
    @allure.feature('Договор')
    @allure.story('Получить документы по договору')
    def test_get_documents_in_agreement(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.issue_agreement()
        agreement.agreement_get_status()
        agreement.get_documents()

