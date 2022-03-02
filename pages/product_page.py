from .base_page import BasePage
from .locators import ProductPageLocators as PPL
from selenium.webdriver.remote.webelement import WebElement


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button: WebElement = self.browser.find_element(*PPL.ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*PPL.ADD_TO_CART), "Adding to cart button is not presented"

    def should_be_add_to_cart_message_with_name(self):
        assert (self.text_of_element(*PPL.ADD_TO_CART_MESSAGE) == self.text_of_element(*PPL.PRODUCT_NAME)), \
            'Wrong message after adding item to card. No name present'

    def should_be_add_to_cart_message_with_price(self):
        assert (self.text_of_element(*PPL.PRODUCT_PRICE) == self.text_of_element(*PPL.CART_PRICE_MESSAGE)), \
            'Wrong message after adding item to card. No price present'
