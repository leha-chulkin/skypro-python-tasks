from selenium import webdriver
from selenium.webdriver.common.by import By

# Используем Firefox
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
# На странице есть поле ввода
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")  # или по другом селектору

# Ввести "Sky"
input_field.send_keys("Sky")

# Очистить поле
input_field.clear()

# Ввести "Pro"
input_field.send_keys("Pro")

# Закрыть браузер
driver.quit()