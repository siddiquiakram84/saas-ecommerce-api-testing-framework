import pytest
import allure

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_report_dir = 'reports'
