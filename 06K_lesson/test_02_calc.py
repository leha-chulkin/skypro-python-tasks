import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator_with_delay(driver):
    wait = WebDriverWait(driver, 60)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Ввод задержки
    delay_input = wait.until(EC.element_to_be_clickable((By.ID, 'delay')))
    delay_input.clear()
    delay_input.send_keys('45')  # Установка задержки, чтобы тест был устойчивым
    
    # XPath для результата
    result_xpath = '//*[@id="result"]'
    
    # XPaths для нажатия (подтвердите их актуальность)
    xpaths = [
        '//*[@id="calculator"]/div[2]/span[1]',  # пример, проверьте, что эти XPaths действительны
        '//*[@id="calculator"]/div[2]/span[4]',
        '//*[@id="calculator"]/div[2]/span[2]',
        '//*[@id="calculator"]/div[2]/span[15]',
    ]
    
    # Проходим по кнопкам и кликаем
    for xpath in xpaths:
        button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        # Можно добавить небольшую задержку, если нужно
        # time.sleep(0.2)
    
    # XPath селекторы для кнопок
    selectors = {
        '7': "//span[@class='btn btn-outline-primary' and text()='7']",
        '8': "//span[@class='btn btn-outline-primary' and text()='8']",
        '+': "//span[@class='operator btn btn-outline-success' and text()='+']",
        '=': "//span[@class='btn btn-outline-warning' and text()='=']"
    }
    
    # Нажимаем "7", "+", "8", "="
    for label in ['7', '+', '8', '=']:
        button = wait.until(EC.element_to_be_clickable((By.XPATH, selectors[label])))
        # Для кнопки "=" используем JavaScript для надежности
        if label == '=':
            driver.execute_script("arguments[0].click();", button)
        else:
            button.click()
    
    # Ждем, пока результат станет "15"
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR, ".screen").text == "15")
    
    # Проверяем результат
    result = driver.find_element(By.CSS_SELECTOR, ".screen")
    assert result.text == "15"
