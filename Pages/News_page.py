from playwright.sync_api import expect
from .Base_page import BasePage


class NewsPage(BasePage):
    def __init__(self,page):
        super().__init__(page)


    @property
    def tags_block(self):
         return self.page.locator('//div[@class="news-tags-list_tags__KVfgf"]')

    def title_block(self):
        return self.page.locator('//h2[@class="page-heading-title_page_heading__title___WsFU"]')

    def tag(self):
        return self.page.locator('//div[@class="news-tags-list_tags__KVfgf"]//button[text()="Культура"]')



    def check_tags_block(self, isvisible=True):
        expect(self.tags_block).to_be_visible(visible=isvisible)
        return isvisible

    def check_title_block(self, isvisible=True):
        expect(self.title_block).to_be_visible(visible=isvisible)
        return isvisible

    def click_to_tag(self):
        self.tag().click()

    def check_text_title(self):
        element = self.title_block()
        return element.text_content()
