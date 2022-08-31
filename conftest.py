import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language_name', action='store', default='es',
                     help="Choose language: es, ru, fr, etc...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def user_language(request):
    browser_name = request.config.getoption("browser_name")
    language_name = request.config.getoption("language_name")
    if browser_name == "chrome":
        print(f"\nchrome + {language_name}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language_name)
    return language_name
