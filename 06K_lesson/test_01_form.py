import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    # Запускаем браузер Edge или Safari
    # Для Edge:
    # driver = webdriver.Edge()
    # Для Safari:
    driver = webdriver.Safari()

    wait = WebDriverWait(driver, 10)  # явное ожидание

    try:
        # Шаг 1: Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        # Шаг 2: Заполнить форму
        driver.find_element(By.NAME, "first_name").send_keys("Иван")
        driver.find_element(By.NAME, "last_name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставить пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        # Выбрать страну (если есть select), предположим, что это поле с именем country
        country_select = driver.find_element(By.NAME, "country")
        for option in country_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == "Россия":
                option.click()
                break
        # Выбрать позицию работы
        job_select = driver.find_element(By.NAME, "job_position")
        for option in job_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == "QA":
                option.click()
                break
        driver.find_element(By.NAME, "company").send_keys("SkyPro")
        
        # Шаг 3: Нажать кнопку Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Ждать некоторое время, чтобы стили обновились
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-field")))  # Подождать появления полей

        # Шаг 4: Проверить подсветку полей

        # Цвет подсветки можно определить через свойство CSS 'background-color' или 'border-color'
        # Предположим, что используется border-color
        def get_field_border_color(element):
            return element.value_of_css_property('border-color')

        # Поле Zip code — должно быть подсвечено красным (например, border-color rgb(255, 0, 0))
        zip_field = driver.find_element(By.NAME, "zip_code")
        zip_border_color = get_field_border_color(zip_field)
        assert zip_border_color in ("rgb(255, 0, 0)", "#ff0000", "red"), "Zip code не подсвечено красным"

        # Остальные поля — зелёным (например, rgb(0, 128, 0))
        # Перечислим остальные поля и проверим их цвет
        fields_to_check = [
            driver.find_element(By.NAME, "first_name"),
            driver.find_element(By.NAME, "last_name"),
            driver.find_element(By.NAME, "address"),
            driver.find_element(By.NAME, "email"),
            driver.find_element(By.NAME, "phone"),
            driver.find_element(By.NAME, "city"),
            # Поле country (может быть select)
            driver.find_element(By.NAME, "country"),
            driver.find_element(By.NAME, "job_position"),
            driver.find_element(By.NAME, "company")
        ]

        for field in fields_to_check:
            color = get_field_border_color(field)
            assert color in ("rgb(0, 128, 0)", "#008000", "green"), f"Поле {field.get_attribute('name')} не подсвечено зелёным"

    finally:
        driver.quit()
