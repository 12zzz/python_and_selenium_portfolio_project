import pytest

from .pages.product_page import ProductPage
import time

base_link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
#link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
bad_links = []
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(0) if no not in bad_links]
bad_urls = [f"{product_base_link}/?promo=offer{no}" for no in bad_links]
#urls.extend(pytest.param(bad_urls, marks=pytest.mark.xfail))

#@pytest.mark.parametrize('promo', [pytest.param('', marks=pytest.mark.xfail(i==7, reason='bad 7 link')) for i in range(10)])


@pytest.mark.parametrize('link',
                         urls+list(map(lambda x: pytest.param(x, marks=pytest.mark.xfail(strict=True)), bad_urls)))
def test_guest_can_add_product_to_basket(browser, link):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    print(link)
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
