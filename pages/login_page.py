from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """Проверка на корректный url адрес,
        есть форма логина,
        есть форма регистрации"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка на корректный url адрес"""
        assert 'login' in self.browser.current_url, 'Нет login в url'

    def should_be_login_form(self):
        """Проверка, что есть форма логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма логина не найдена'

    def should_be_register_form(self):
        """Проверка, что есть форма регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма регистрации не найдена'

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
