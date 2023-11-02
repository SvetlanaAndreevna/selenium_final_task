from selenium.webdriver.common.by import By

# каждый селектор в классе— это пара: как искать и что искать
class MainPageLocators:
    pass

class BasePageLocators:
    # кнопка для входа
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # значок зарегистрированного пользователя
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    # форма для ввода логина и пароля
    LOGIN_FORM = (By.ID, 'login_form')
    # форма для регистрации
    REGISTER_FORM = (By.ID, 'register_form')
    # поле регистрации для ввода email
    REGISTRATION_EMAIL = (By.NAME, 'registration-email')
    # поле регистрации для ввода пароля
    REGISTRATION_PASSWORD1 = (By.NAME, 'registration-password1')
    # поле регистрации для повторного ввода пароля
    REGISTRATION_PASSWORD2 = (By.NAME, 'registration-password2')
    # КНОПКА ЗАРЕГИСТРИРОВАТЬСЯ
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    # кнопка добавления в корзину
    BUTTON_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    # имя продукта
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    # имя добавленного в корзину продукта
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages .alertinner:nth-child(2) strong')
    # сообщение '... добавлен в вашу корзину'
    MESSAGE_ADD = (By.CSS_SELECTOR, '#messages .alertinner:nth-child(2) ')
    # сообщение 'Стоимость корзины ...'
    MESSAGE_ABOUT_PRICE_BASKET = (By.CSS_SELECTOR, '#messages .alertinner p')
    # цена корзины
    PRICE_BASKET = (By.CSS_SELECTOR, '#messages .alertinner p strong')
    # цена продукта
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')

class BasketPageLocators:
    # кнопка для перехода в корзину в шапке сайта
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, '.basket-mini a.btn')
    # товары в корзине
    PRODUCTS_IN_BASKET = (By.CLASS_NAME, 'basket_summary')
    # сообщение о том, что корзина пуста
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')