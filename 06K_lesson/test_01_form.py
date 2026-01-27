# test_01_form.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера"""
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    """Фикстура для явных ожиданий"""
    return WebDriverWait(driver, 10)


def test_form_validation(driver, wait):
    """
    Тест валидации формы на странице https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    
    Шаги теста:
    1. Открыть страницу в Edge
    2. Заполнить форму значениями
    3. Нажать кнопку Submit
    4. Проверить, что поле Zip code подсвечено красным
    5. Проверить, что остальные поля подсвечены зеленым
    """
    # Шаг 1: Открыть страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)
    
    # Ожидаем загрузки страницы и появления формы
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    
    # Шаг 2: Заполнить форму значениями
    test_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",  # Оставить пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    
    # Заполняем каждое поле
    for field_name, value in test_data.items():
        field = wait.until(EC.presence_of_element_located((By.NAME, field_name)))
        field.clear()
        if value:  # Отправляем значение только если оно не пустое
            field.send_keys(value)
    
    # Шаг 3: Нажать кнопку Submit
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    
    # Прокручиваем к кнопке и кликаем через JavaScript для надежности
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    
    # Ждем появления подсветки полей
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success")))
    
    # Шаг 4: Проверить, что поле Zip code подсвечено красным
    zip_code_element = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    zip_code_class = zip_code_element.get_attribute("class")
    
    # Проверяем наличие красной подсветки (alert-danger - стандартный класс Bootstrap для ошибок)
    assert "alert-danger" in zip_code_class, (
        f"Поле Zip code должно быть подсвечено красным (содержать 'alert-danger'). "
        f"Текущий класс: '{zip_code_class}'"
    )
    
    # Шаг 5: Проверить, что остальные поля подсвечены зеленым
    green_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]
    
    for field_id in green_fields:
        field_element = wait.until(EC.presence_of_element_located((By.ID, field_id)))
        field_class = field_element.get_attribute("class")
        
        # Проверяем наличие зеленой подсветки (alert-success - стандартный класс Bootstrap для успеха)
        assert "alert-success" in field_class, (
            f"Поле '{field_id}' должно быть подсвечено зеленым (содержать 'alert-success'). "
            f"Текущий класс: '{field_class}'"
        )
    
    # Дополнительная проверка: подсчитаем количество зеленых и красных полей
    green_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
    red_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
    
    assert len(green_elements) == 9, f"Должно быть 9 зеленых полей, найдено {len(green_elements)}"
    assert len(red_elements) == 1, f"Должно быть 1 красное поле, найдено {len(red_elements)}"


if __name__ == "__main__":
    # Для запуска напрямую (если нужно)
    pytest.main([__file__, "-v"])
