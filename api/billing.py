import requests

class BillingAPI:
    def __init__(self, api_gateway):
        self.base_url = f"{api_gateway}/admin/v1/billing/tenant"

    def get_cards(self, tenant_id):
        url = f"{self.base_url}/cards"
        payload = {"tenant_id": tenant_id}
        response = requests.get(url, json=payload)
        return response
