from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_element)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    rb_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotsRule")

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    rb_checkbox.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
