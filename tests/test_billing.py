import pytest
import allure
from api.billing import BillingAPI
from data.test_data import test_data
from utils.allure_report import attach_request_and_response

@pytest.fixture(scope="module")
def billing_api():
    api_gateway = "http://your-api-gateway-url"
    return BillingAPI(api_gateway)

@allure.feature("Billing API")
@allure.story("Get Tenant Cards")
def test_get_tenant_cards(billing_api):
    with allure.step("Send GET request to retrieve tenant cards"):
        response = billing_api.get_cards(test_data["tenant_id"])

    with allure.step("Attach request and response details to Allure report"):
        attach_request_and_response(response.request, response)

    with allure.step("Validate the response"):
        assert response.status_code == 200
        assert "cards" in response.json()
