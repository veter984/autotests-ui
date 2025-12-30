from playwright.sync_api import Page, expect
from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')


    #def fill_registration_form(self, email: str, username: str, password: str):
        #self.email_input.fill(email)
        #expect(self.email_input).to_have_value(email)

        #self.username_input.fill(username)
        #expect(self.username_input).to_have_value(username)

        #self.password_input.fill(password)
        #expect(self.password_input).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()


