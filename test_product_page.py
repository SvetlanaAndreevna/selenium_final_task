from pages.product_page import ProductPage
import pytest
import time

# ФАЙЛ С ТЕСТАМИ ДЛЯ СТРАНИЦЫ ТОВАРА


url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

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
def test_guest_can_add_product_to_basket(browser, link):
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
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Тест на непоявление в течение заданного времени cообщения о доб. в корзину
    после добавления товара в корзину"""
    page = ProductPage(browser, url)
    page.open()
    page.product_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_message_about_add_to_basket()


def test_guest_cant_see_success_message(browser):
    """Тест на непоявление в течение заданного времени cообщения о доб. в корзину
    до добавления товара в корзину"""
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_message_about_add_to_basket()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Тест на исчезание в течение заданного времени cообщения о доб. в корзину
    после добавления товара в корзину"""
    page = ProductPage(browser, url)
    page.open()
    page.product_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_is_disappeared()

# pytest -v -s test_product_page.py
# команда для запуска
