from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time
import random

# ФАЙЛ С ТЕСТАМИ ДЛЯ СТРАНИЦЫ ТОВАРА


url = 'http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/'


class TestGuestAddToBasketFromProductPage:
    """Класс тестов для незарегистрированного пользователя"""

    @pytest.mark.smoke
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        """Smoke тест на возможность добавления товара в корзину и
        корректность отображаемых после этого сообщений"""
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket()
        page.product_add_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(3)
        page_after_add = ProductPage(browser, browser.current_url)
        page_after_add.should_be_message_about_add_to_basket()
        page_after_add.true_name_product_in_message_about_add_to_basket()
        page_after_add.should_be_message_about_price_basket()
        page_after_add.true_price_basket()


    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """Тест на непоявление в течение заданного времени cообщения о доб. в корзину
        после добавления товара в корзину"""
        page = ProductPage(browser, url)
        page.open()
        page.product_add_to_basket()
        page.should_not_be_message_about_add_to_basket()


    def test_guest_cant_see_success_message(self, browser):
        """Тест на непоявление в течение заданного времени cообщения о доб. в корзину
        до добавления товара в корзину"""
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_message_about_add_to_basket()


    @pytest.mark.skip
    def test_guest_message_disappeared_after_adding_product_to_basket(self, browser):
        """Тест на исчезание в течение заданного времени cообщения о доб. в корзину
        после добавления товара в корзину"""
        page = ProductPage(browser, url)
        page.open()
        page.product_add_to_basket()
        page.should_is_disappeared()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, url)
        page.open()
        page.go_to_basket()
        page_basket = BasketPage(browser, browser.current_url)
        page_basket.should_be_empty_basket()
        page_basket.should_be_message_about_empty_basket()

@pytest.mark.new
class TestUserAddToBasketFromProductPage:
    """Класс тестов для зарегистрированного пользователя"""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Фикстура для регистрации нового пользователя и проверки, что регистрация прошла успешно"""
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = f"{random.choice('qwertyuiop')}{random.randint(1111, 9999)}@fakermail.com"
        password = str(random.randint(111111111, 999999999))
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        """Smoke тест на возможность добавления товара в корзину и
        корректность отображаемых после этого сообщений"""
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket()
        page.product_add_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(3)
        page_after_add = ProductPage(browser, browser.current_url)
        page_after_add.should_be_message_about_add_to_basket()
        page_after_add.true_name_product_in_message_about_add_to_basket()
        page_after_add.should_be_message_about_price_basket()
        page_after_add.true_price_basket()

    def test_user_cant_see_success_message(self, browser):
        """Тест на непоявление в течение заданного времени cообщения о доб. в корзину
        до добавления товара в корзину"""
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_message_about_add_to_basket()

# pytest -v -s test_product_page.py
# команда для запуска
