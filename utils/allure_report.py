import allure

def attach_request_and_response(request, response):
    with allure.step("Request"):
        allure.attach(request.method + ' ' + request.url, 'Request URL and Method', allure.attachment_type.TEXT)
        allure.attach(str(request.headers), 'Request Headers', allure.attachment_type.TEXT)
        allure.attach(str(request.body), 'Request Body', allure.attachment_type.JSON)

    with allure.step("Response"):
        allure.attach(str(response.status_code), 'Response Status Code', allure.attachment_type.TEXT)
        allure.attach(str(response.headers), 'Response Headers', allure.attachment_type.TEXT)
        allure.attach(response.text, 'Response Body', allure.attachment_type.JSON)
