import pytest

from .pages.product_page import ProductPage
import time

#link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
bad_links = [7, 8]
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(3) if no not in bad_links]
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

