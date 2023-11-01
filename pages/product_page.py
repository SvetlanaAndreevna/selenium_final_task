from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def product_add_to_basket(self):
        """Добавление товара в корзину"""
        self.browser.find_element(*ProductPageLocators.BUTTON_BASKET).click()

    def should_be_add_to_basket(self):
        """Проверка наличия кнопки добавления в корзину"""
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET), 'Кнопка для добавления в корзину не найдена'

    def should_be_message_about_add_to_basket(self):
        """Проверка наличия сообщения о том, что товар добавлен в корзину"""
        message_add = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD).text
        assert message_add, 'Нет сообщения о том, что товар добавлен в корзину'

    def true_name_product_in_message_about_add_to_basket(self):
        """Проверка, что имя добавляемого товара совпадает с именем товара в сообщении о добавлении в корзину"""
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text
        assert name_product_in_basket == name_product, 'Имя товара не совпадает с именем товара в сообщении'

    def should_be_message_about_price_basket(self):
        """Проверка наличия сообщения о стоимости корзины"""
        message_about_price_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_PRICE_BASKET).text
        assert message_about_price_basket, 'Нет сообщения о стоимости корзины'

    def true_price_basket(self):
        """Проверка, что стоимость корзины равна стоимости добавленного товара"""
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_product == price_basket, 'Стоимость корзины не равна стоимости добавленного товара'
