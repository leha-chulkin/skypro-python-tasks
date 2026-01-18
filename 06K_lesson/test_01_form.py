import pytest
from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submit(driver: Any):
    wait = WebDriverWait(driver, 10)
    driver.get("http://example.com/form")  # поменяйте на ваш URL

    wait.until(
        EC.visibility_of_element_located((By.ID, 'name'))
    ).send_keys('Имя')
    driver.find_element(By.ID, 'email').send_keys('test@example.com')
    driver.find_element(By.ID, 'submit').click()

    confirmation = wait.until(
        EC.visibility_of_element_located((By.ID, 'confirmation'))
    )
    assert 'Success' in confirmation.text
