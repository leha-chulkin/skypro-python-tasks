from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")
# В этом примере на странице есть кнопка с текстом или классом
# Предположим, кнопку можно найти по CSS-селектору
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()

driver.quit()