from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    TO_CART_LINK = (By.XPATH, '//span/a[@href="/en-gb/basket/"]')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_CONFIRM_MESSAGE = (By.CSS_SELECTOR, '.alertinner.wicon')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_BUTTON = (By.XPATH, '//button[@value="Register"]')


class ProductPageLocators:
    SUCCESS_MESSAGE_CLOSE = (By.CSS_SELECTOR, '.alert-success .close')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages .alert strong')
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(3).alert strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')


class BasketPageLocators:
    CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner>p>a')
    NO_ITEMS_IN_CART = (By.CSS_SELECTOR, '#.basket-items')
