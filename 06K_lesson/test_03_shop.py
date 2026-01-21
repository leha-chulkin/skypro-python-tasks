from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    print("Открытие сайта...")
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    print("Авторизация...")
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    print("Добавление товаров в корзину...")
    # Используем By.ID
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    print("Добавлен Sauce Labs Backpack.")
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    print("Добавлен Sauce Labs Bolt T-Shirt.")
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()
    print("Добавлен Sauce Labs Onesie.")

    print("Переход в корзину...")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    print("Оформление заказа...")
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    print("Заполнение формы...")
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    print("Получение итоговой суммы...")
    total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text.strip()
    print(f"Итоговая сумма на странице: {total_text}")

    # Проверка суммы
    expected_sum = "$58.29"
    if expected_sum in total_text:
        print("Тест прошёл успешно — сумма совпадает.")
    else:
        print("Сумма не совпадает.")
finally:
    print("Закрытие браузера...")
    driver.quit()
    print("Браузер закрыт.")
