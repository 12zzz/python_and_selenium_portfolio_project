from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import math
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: WebDriver, url, timeout=3):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except exceptions.TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def text_of_element(self, how: By, what: str):
        try:
            text = self.browser.find_element(how, what)
        except exceptions.NoSuchElementException:
            return False
        return text.text

    def alert_is_present(self, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
        except exceptions.TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):

        # Method for promo pages with quiz

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except exceptions.NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except exceptions.TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, exceptions.TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except exceptions.TimeoutException:
            return False

        return True

    def go_to_cart(self):
        link = self.browser.find_element(*BasePageLocators.TO_CART_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def send_keys(self, by, value, keys):
        link = self.browser.find_element(by, value)
        link.send_keys(keys)
