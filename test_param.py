import pytest
from selenium.webdriver.common.by import By
import time
import math


@pytest.mark.parametrize('num', ["236895", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, num):
    browser.implicitly_wait(5)
    link = f"https://stepik.org/lesson/{num}/step/1"
    browser.get(link)
    textarea = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
    answer = math.log(int(time.time()))
    textarea.send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    current = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert current == "Correct!", f"Current: {current}"
    print(current)

#  browser.find_element(By.CSS_SELECTOR, "#login_link")
# answer = math.log(int(time.time()))
