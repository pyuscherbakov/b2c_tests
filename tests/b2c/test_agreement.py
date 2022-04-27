from core.api.agreements.agreements import Agreement
from core.api.contracts.contracts import Contract
import allure
import pytest


@pytest.mark.parametrize("product", [
    # "ingos_kasko",
    "alfastrah_kasko"
])
@pytest.mark.parametrize("franchise", [
    "Нет",
    "Безусловная 15 тыс."
])
class TestAgreement:

    @allure.feature('Договор')
    @allure.story('Создать договор')
    @allure.title('Создать договор')
    def test_create_agreement(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.attach_agreement_data()

    @allure.feature('Договор')
    @allure.story('Получить договор')
    @allure.title('Получить договор со статусом Draft')
    # TODO: реализовать получение договора в статусе Issued
    def test_get_agreement_with_status_draft(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.get_agreement("Draft")
        agreement.attach_agreement_data()

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
        agreement.attach_agreement_data()

    @allure.feature('Договор')
    @allure.story('Договор - статус выполнения операции')
    @allure.title('Договор - статус выполнения операции')
    def test_task_agreement(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        agreement.issue_agreement()
        agreement.agreement_get_status()
        agreement.attach_agreement_data()

    @allure.feature('Договор')
    @allure.story('Получить документы по договору')
    @allure.title('Получить документы по договору')
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
        agreement.attach_agreement_data()

    @allure.feature('Договор')
    @allure.story('Оформить договор')
    @allure.title('Оформить договор')
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
        agreement.attach_agreement_data()

    # TODO: Проверить
    @pytest.mark.skip(reason="Тест не проверен, так как альфа упала")
    @allure.feature('Договор')
    @allure.story('Обновить договор')
    @allure.title('Обновить договор')
    def test_update_agreement(self, product, franchise):
        contract = Contract(franchise)
        contract.create_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement = Agreement(contract.get_contract_id(), product)
        agreement.create_agreement()
        contract.update_contract("purchase_date")
        contract.get_updated_contract()
        contract.create_calculation(product)
        contract.get_calculation()
        agreement.update_agreement()
        agreement.agreement_get_status()
        agreement.get_updated_agreement()
