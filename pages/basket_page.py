from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        """Проверка, что корзина пуста"""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), 'Корзина не пуста'

    def should_be_message_about_empty_basket(self):
        """Проверка наличия сообщения о том, что корзина пуста"""
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), 'Нет сообщения о том, что корзина пуста'
