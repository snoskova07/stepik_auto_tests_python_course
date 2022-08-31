from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            firstname = browser.find_element(By.XPATH,
                                             "//div[@class='first_block']//div[@class='form-group first_class']//input[@type='text']")

            firstname.send_keys("Sv")
            lastname = browser.find_element(By.XPATH,
                                            "//div[@class='first_block']//div[@class='form-group second_class']//input[@type='text']")
            lastname.send_keys('N')
            email = browser.find_element(By.XPATH,
                                         "//div[@class='first_block']//div[@class='form-group third_class']//input[@type='text']")
            email.send_keys('sv@dds.dd')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Wrong")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(2)
            # закрываем браузер после всех манипуляций
            browser.quit()


    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            firstname = browser.find_element(By.XPATH,
                                             "//div[@class='first_block']//div[@class='form-group first_class']//input[@type='text']")

            firstname.send_keys("Sv")
            lastname = browser.find_element(By.XPATH,
                                            "//div[@class='first_block']//div[@class='form-group second_class']//input[@type='text']")
            lastname.send_keys('N')
            email = browser.find_element(By.XPATH,
                                         "//div[@class='first_block']//div[@class='form-group third_class']//input[@type='text']")
            email.send_keys('sv@dds.dd')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Wrong")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(2)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
