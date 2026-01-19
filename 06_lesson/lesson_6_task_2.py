from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Создаём драйвер один раз
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/textinput')

try:
    # Ждём, пока кнопка станет кликабельной
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'updatingButton'))
    )
    button.click()

    # Ждём, пока текст кнопки изменится на "SkyPro"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'updatingButton'), 'SkyPro')
    )

    # Получаем обновлённый элемент и выводим его текст
    updated_button = driver.find_element(By.ID, 'updatingButton')
    print(updated_button.text)
finally:
    driver.quit()
