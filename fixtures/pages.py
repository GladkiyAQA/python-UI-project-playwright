import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.fixture()
def login_page(chromium_browser: Page) -> LoginPage:
    return LoginPage(page=chromium_browser)

@pytest.fixture()
def registration_page(chromium_browser: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_browser)

@pytest.fixture()
def dashboard_page(chromium_browser: Page) -> DashboardPage:
    return DashboardPage(page=chromium_browser)