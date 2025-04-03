from playwright.sync_api import expect
from .Base_page import BasePage


class AltPage(BasePage):
    def __init__(self,page):
        super().__init__(page)


    @property
    def button_look_all(self):
         return self.page.locator(
            '//a[@class="golden-years-news-list_golden_years_news__link__TADgK"]//span[text()="Смотреть все"]')

    def check_button_look_all_exists(self, isvisible=True):
        expect(self.button_look_all).to_be_visible(visible=isvisible)

    def click_button_look_all_exists(self):
        self.button_look_all.click()
