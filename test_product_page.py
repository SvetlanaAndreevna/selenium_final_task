from pages.product_page import ProductPage


# ФАЙЛ С ТЕСТАМИ ДЛЯ СТРАНИЦЫ ТОВАРА

def test_guest_can_add_product_in_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_add_to_basket()
    page.true_name_product_in_message_about_add_to_basket()
    page.should_be_message_about_price_basket()
    page.true_price_basket()


def test_should_be_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
