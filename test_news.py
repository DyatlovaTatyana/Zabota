import pytest
from playwright.sync_api import Page, expect
from Pages.Alt_page import AltPage
from Pages.News_page import NewsPage
from Pages.News_card import NewsCard
from Link import Links
import time

@pytest.mark.usefixtures("browser")
class TestNews:
    #Открытие новостей с АлтынЕллар
    def test_1(self, browser: Page):
        alt_page = AltPage(browser)
        news_page = NewsPage(browser)
        alt_page.open(Links.ALTELL)
        alt_page.check_button_look_all_exists()
        alt_page.click_button_look_all_exists()
        news_page.check_tags_block()
        assert news_page.check_tags_block() == True
        # assert news_page.check_title_block() == True

    # Применение фильтров из блока популярных тем
    def test_2(self, browser: Page):
        news_page = NewsPage(browser)
        news_page.open(Links.NEWS_PAGE)
        news_page.click_to_tag()
        # assert news_page.check_text_title() == "Культура – последние новости"
        assert "– последние новости" in news_page.check_text_title()
        assert news_page.check_tags_block(False) == False #Хз как это сработало,верно ли вообще такую проверку делать?

    # Применение фильтров из карточки новости
    def test_3(self, browser: Page):
        news_page = NewsPage(browser)
        news_card = NewsCard(browser)
        news_card.open(Links.NEWS_CARD)
        news_card.click_to_tag()
        time.sleep(5)
        assert "– последние новости" in news_page.check_text_title() #Тут такая же проверка как и во втором тесте. Падает без слипов, почему?
