from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, timeout= 10)

    data = {
        "First name": "Иван",
        "Last name": "Петров",
        "Address": "Ленина, 55-3",
        "Email": "test@skypro.com",
        "Phone": "+7985899998787",
        "Zip code": "",
        "City": "Москва",
        "Country": "Россия",
        "Job position": "QA",
        "Company": "SkyPro",
    }

    for field, value in data.items():
        Element = wait.until(
            EC.presence_of_all_elements_located((By.NAME, field))
        )
        Element.clear()
        Element.send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "value:button[type= 'subait']").click()

    zip_field = wait.until(
        EC.presence_of_elements_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_field.get_attribute("class")

    green_fields = [
        "First name",
        "Last name",
        "Address",
        "Email",
        "Phone",
        "City",
        "Country",
        "Job position",
        "Company",
    ]

    for field in green_fields:
        Element = driver.find_element(By.ID,field)
        assert "alert-success" in Element.get_attribute("class")

    driver.quit()
