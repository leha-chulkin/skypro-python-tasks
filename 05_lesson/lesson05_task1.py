from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера Chrome
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/classattr")
# Клик по кнопке с CSS-классом 'btn-primary'
button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

# Закрытие браузера
driver.quit()