from playwright.sync_api import Page
from elements.button import Button
from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', 'Menu')
        self.edit_menu_item = Button(page, 'course-view-edit-menu-item', 'Edit')
        self.delete_menu_item = Button(page, 'course-view-delete-menu-item', 'Delete')

        #self.menu_button = page.get_by_test_id('course-view-menu-button')
        #self.edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        #self.delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

        #self.menu_button.nth(index).click()

        #expect(self.edit_menu_item.nth(index)).to_be_visible()
        #self.edit_menu_item.nth(index).click()

    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index)

        #self.menu_button.nth(index).click()

        #expect(self.delete_menu_item.nth(index)).to_be_visible()
        #self.delete_menu_item.nth(index).click()