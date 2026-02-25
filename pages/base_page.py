from playwright.sync_api import Page, expect
from typing import Pattern
import allure
from config import settings
from enum import Enum


class BasePage:
    def __init__(self, page: Page):
        self.page = page


    def visit(self, url: str | Enum):
        if hasattr(url, 'value'):
            url = url.value


        base_url = str(settings.app_url).rstrip('/')
        if url.startswith('#/'):
            full_url = f"{base_url}{url}"  # https://.../#/auth/registration
        else:
            full_url = f"{base_url}/{url.lstrip('/')}"


        with allure.step(f'Opening the url "{full_url}"'):
            self.page.goto(full_url, wait_until='networkidle')



        #with allure.step(f'Opening the url "{url}"'):
            #self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)