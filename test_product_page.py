import pytest

import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

base_link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"  # link for quiz task
bad_links = [7]
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(1) if no not in bad_links]
# Only 1 link in urls "range(1)", not 10 because we already know bad link, not need 10 identical test
bad_urls = [f"{product_base_link}/?promo=offer{no}" for no in bad_links]


@pytest.mark.parametrize('link',
                         urls + list(map(lambda x: pytest.param(x, marks=pytest.mark.xfail(strict=True)), bad_urls)))
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_cart_message_with_name()
    page.should_be_add_to_cart_message_with_price()


@pytest.mark.lesson436
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


@pytest.mark.lesson436
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.lesson436
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_message()


@pytest.mark.to_login_page
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.to_login_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.go_to_login_page()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.go_to_cart()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.text_no_items_in_cart()
    basket_page.check_no_items_in_cart()


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email, "Somepassword")
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        promo_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, promo_link)
        page.open()
        page.should_be_add_to_cart_button()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_add_to_cart_message_with_name()
        page.should_be_add_to_cart_message_with_price()

    def test_user_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, base_link)
        page.open()
        page.should_not_be_success_message()
