from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/ajax")
    wait = WebDriverWait(driver, 10)

    # Нажать кнопку
    button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button#ajaxButton")
        )
    )
    button.click()

    # Получить текст из зеленой плашки
    message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div#content div.alert-success")
        )
    )
    print("Data loaded with AJAX get request.")
    print(message.text)
finally:
    driver.quit()
