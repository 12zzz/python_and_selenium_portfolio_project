from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    #LOGIN_URL = (By.CSS_SELECTOR, '')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    SUCCESS_MESSAGE_CLOSE = (By.CSS_SELECTOR, '.alert-success .close')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages .alert strong')
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(3).alert strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
