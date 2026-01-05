import pytest
from playwright.sync_api import Page, Playwright, expect

from pages.login_page import LoginPage
from components.authentication.login_form_component import LoginFormComponent

@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "passsword"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(login_page: Page, email, password):

    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_page.login_form.fill(email=email, password=password)
    login_page.login_form.check_visible(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
    #chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    #email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    #email_input.fill(email)

    #password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    #password_input.fill(password)

    #login_button = chromium_page.get_by_test_id('login-page-login-button')
    #login_button.click()

    #wrong_email_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    #expect(wrong_email_password_alert).to_be_visible()
    #expect(wrong_email_password_alert).to_have_text('Wrong email or password')

