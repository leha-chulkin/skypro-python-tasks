import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shop_total(driver):
    wait = WebDriverWait(driver, 10)
    
    # Открытие сайта
    print("Открытие сайта saucedemo.com...")
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    print("Авторизация...")
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # Добавление товаров в корзину
    print("Добавление товаров в корзину...")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]'))).click()

    # Переход в корзину и оформление заказа
    print("Переход в корзину...")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    print("Оформление заказа...")
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Заполнение формы
    print("Заполнение формы...")
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Проверка итоговой суммы
    print("Проверка итоговой суммы...")
    total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text.strip()
    print(f"Итоговая сумма: {total_text}")
    
    expected_sum = "$58.29"
    assert expected_sum in total_text, f"Ожидалось '{expected_sum}', но получено '{total_text}'"
    print("✅ Тест пройден успешно — сумма совпадает!")
