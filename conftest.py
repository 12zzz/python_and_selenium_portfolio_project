import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store',  default=en,
                     help="Choose language. For example: ru")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    browser_lang = request.config.getoption("language").rsplit(" ")[0]

    browser = None
    if browser_lang:
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("Script should run with --language your_language command")
    yield browser
    browser.quit()
