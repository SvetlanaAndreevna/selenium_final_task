from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


# ФАЙЛ С ТЕСТАМИ ДЛЯ ГЛАВНОЙ СТРАНИЦЫ

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """Тест, что с главной страницы
        по кнопке для входа переходим по корректному url адресу, где
        есть форма логина и
        есть форма регистрации"""
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)  # создаем объект нужного класса с актуальным url
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """Тест на наличие кнопки для входа"""
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Тест на то, что при переходе с главной страницы в корзину
    корзина будет пуста и будет сообщение об этом"""
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_empty_basket()
    page_basket.should_be_message_about_empty_basket()


# pytest -v --tb=line --language=en test_main_page.py
# команда для запуска
