import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping_process(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Добавление товаров
    products = [
        'sauce-backpack',
        'sauce-bolt-t-shirt',
        'sauce-onesie'
    ]

    for product_id in products:
        btn = wait.until(EC.element_to_be_clickable((By.ID, f'add-to-cart-{product_id}')))
        btn.click()

    # Перейти в корзину
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))).click()

    # Checkout
    wait.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

    # Заполнение формы
    wait.until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys('Имя')
    driver.find_element(By.ID, 'last-name').send_keys('Фамилия')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()

    # Проверка итоговой суммы
    total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_subtotal_label')))
    total_text = total_element.text
    # Ожидаемый формат: "Item total: $58.29"
    assert total_text == 'Item total: $58.29'
