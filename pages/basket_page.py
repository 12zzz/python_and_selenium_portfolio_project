from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_no_items_in_cart(self):
        assert self.is_element_present(*BasketPageLocators.CART_IS_EMPTY_TEXT), 'Cart is not empty!'

    def text_no_items_in_cart(self):
        assert self.is_element_present(*BasketPageLocators.CART_IS_EMPTY_TEXT), 'Cart is not empty!'
