from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """проверка на корректный url адрес,
        есть форма логина,
        есть форма регистрации"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """ проверка на корректный url адрес"""
        assert 'login' in self.browser.current_url, 'Нет login в url'

    def should_be_login_form(self):
        """проверка, что есть форма логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма логина не найдена'

    def should_be_register_form(self):
        """проверка, что есть форма регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма регистрации не найдена'