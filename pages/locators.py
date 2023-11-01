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

class ProductPageLocators:
    # кнопка добавления в корзину
    BUTTON_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    # имя продукта
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    # имя добавленного в корзину продукта
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages .alertinner:nth-child(2) strong')
    # сообщение '... добавлен в вашу корзину'
    MESSAGE_ADD = (By.CSS_SELECTOR, '##messages .alertinner:nth-child(2) ')
    # сообщение 'Стоимости корзины ...'
    MESSAGE_ABOUT_PRICE_BASKET = (By.CSS_SELECTOR, '#messages .alertinner p')
    # цена корзины
    PRICE_BASKET = (By.CSS_SELECTOR, '#messages .alertinner p strong')
    # цена продукта
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
