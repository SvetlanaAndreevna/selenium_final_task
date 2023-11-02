from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, BasketPageLocators
import math


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # командa для неявного ожидания

    def open(self):
        """Метод для перехода по ссылке"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Метод для проверки существования элемента"""
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Метод для проверки, что элемент не появляется в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Метод для проверки, что элемент исчезает в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        """Метод для перехода на страницу с формой входа и регистрации"""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Проверка наличия кнопки для входа"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Кнопка для входа не найдена'

    def go_to_basket(self):
        """Переход в корзину по кнопке в шапке сайта"""
        try:
            self.browser.find_element(*BasketPageLocators.BUTTON_GO_TO_BASKET).click()
        except NoSuchElementException:
            print('Кнопка для просмотра корзины не найдена')

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'Значок пользователя не отображается. Вероятно, неавторизованный пользователь'

    def solve_quiz_and_get_code(self):
        """Метод для получения проверочного кода.
        Запускайть PyTest в консоли с параметром -s"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
