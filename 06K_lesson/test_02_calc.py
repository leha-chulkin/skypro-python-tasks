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

def test_multiple_elements_click(driver):
    wait = WebDriverWait(driver, 60)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Вводим задержку
    delay_input = wait.until(EC.element_to_be_clickable((By.ID, 'delay')))
    delay_input.clear()
    delay_input.send_keys('45')
    
    # XPath результата (проверьте, актуален ли он)
    result_xpath = '//*[@id="result"]'
    
    # Массив XPaths для нажатиия
    xpaths = [
        '//*[@id="calculator"]/div[2]/span[1]',
        '//*[@id="calculator"]/div[2]/span[4]',
        '//*[@id="calculator"]/div[2]/span[2]',
        '//*[@id="calculator"]/div[2]/span[15]',
    ]
    
    # Проходим по элементам и кликаем
    for xpath in xpaths:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    
    # Ждем, пока результат станет равен '15'
    wait.until(EC.text_to_be_present_in_element((By.XPATH, result_xpath), '15'))
    # Или, для дополнительной проверкв, можно взять и Assert
    result_text = driver.find_element(By.XPATH, result_xpath).text
    assert '15' in result_text, f"Expected result '15', but got '{result_text}'"
