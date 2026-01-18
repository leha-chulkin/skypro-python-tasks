from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
# Вводим логин
driver.find_element(By.ID, "username").send_keys("tomsmith")
# Вводим пароль
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
# Нажимаем кнопку login
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Получаем текст зеленой плашки
message = driver.find_element(By.CSS_SELECTOR, "div.flash.success").text
print(message.strip())

driver.quit()