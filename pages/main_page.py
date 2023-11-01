from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def go_to_login_page(self):
        """Переход на страницу с формой входа и регистрации"""
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Проверка наличия кнопки для входа"""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Кнопка для входа не найдена'
