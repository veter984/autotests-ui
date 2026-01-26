from playwright.sync_api import Page
from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from elements.link import Link
from elements.button import Button
import re


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.login_link = Link(page, 'registration-page-login-link', 'Login')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')


    #def fill_registration_form(self, email: str, username: str, password: str):
        #self.email_input.fill(email)
        #expect(self.email_input).to_have_value(email)

        #self.username_input.fill(username)
        #expect(self.username_input).to_have_value(username)

        #self.password_input.fill(password)
        #expect(self.password_input).to_have_value(password)

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))

    def click_registration_button(self):
        self.registration_button.click()


