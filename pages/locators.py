from selenium.webdriver.common.by import By

# каждый селектор в классе— это пара: как искать и что искать
class MainPageLocators:
    # кнопка для входа
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    # форма для ввода логина и пароля
    LOGIN_FORM = (By.ID, 'login_form')
    # форма для регистрации
    REGISTER_FORM = (By.ID, 'register_form')