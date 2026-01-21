import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(driver: WebDriver):
    wait = WebDriverWait(driver, 45)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = wait.until(EC.element_to_be_clickable((By.ID, 'delay')))
    delay_input.clear()
    delay_input.send_keys('45')
    
    # Выполняем операцию 7 + 8 =
    driver.find_element(By.XPATH, "//button[text()='7']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    
    # Проверка, что в результате появилось 15
    wait.until(EC.text_to_be_present_in_element((By.ID, 'result'), '15'))
    result_text = driver.find_element(By.ID, 'result').text
    assert result_text == '15'
