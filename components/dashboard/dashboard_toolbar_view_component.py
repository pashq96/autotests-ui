from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import allure

from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Title')

    @allure.step('Check visible dashboard toolbar view')
    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Dashboard')
