from selenium.webdriver.common.by import By

# каждый селектор в классе— это пара: как искать и что искать
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")