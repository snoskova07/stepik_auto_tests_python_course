import time
from selenium.webdriver.common.by import By


def test_language_param(browser, user_language):
    link = f"https://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"
    browser.get(link)
    button_text = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket").text
    print(button_text)
    print(user_language)
    if user_language == 'es':
        assert button_text == 'Añadir al carrito'
    elif user_language == 'fr':
        assert button_text == 'Ajouter au panier'
    elif user_language == 'ru':
        assert button_text == 'Добавить в корзину'

    time.sleep(2)
