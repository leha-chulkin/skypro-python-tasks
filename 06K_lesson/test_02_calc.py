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

def test_multiple_elements_click(driver):
    wait = WebDriverWait(driver, 60)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Вводим задержку
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
    
    # Проверяем, что результат обновился
    wait.until(EC.text_to_be_present_in_element((By.XPATH, result_xpath), '15'))
    
    # Получаем текст результата
    result_text = driver.find_element(By.XPATH, result_xpath).text
    assert '15' in result_text, f"Expected result '15', but got '{result_text}'"
