from pages.main_page import MainPage
from pages.login_page import LoginPage

# ФАЙЛ С ТЕСТАМИ ДЛЯ ГЛАВНОЙ СТРАНИЦЫ

def test_guest_can_go_to_login_page(browser):
    """Тест, что с главной страницы
    по кнопке для входа переходим по корректному url адресу, где
    есть форма логина и
    есть форма регистрации"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)  # создаем объект нужного класса с актуальным url
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    """Тест на наличие кнопки для входа"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# pytest -v --tb=line --language=en test_main_page.py
# команда для запуска
