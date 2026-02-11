from playwright.sync_api import Page
from elements.Image import Image
from elements.text import Text
from components.base_component import BaseComponent
import allure

class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        #self.identifier = identifier

        #self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        #self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')
        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible chart view "{title}"')
    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()
    #def check_visible(self):

        #expect(self.title).to_be_visible()

        #expect(self.title).to_have_text(self.identifier.capitalize())
        #expect(self.chart).to_be_visible()

