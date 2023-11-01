from pages.product_page import ProductPage
import time


# ФАЙЛ С ТЕСТАМИ ДЛЯ СТРАНИЦЫ ТОВАРА

def test_guest_can_add_product_in_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
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


# pytest -v -s test_product_page.py
# команда для запуска
