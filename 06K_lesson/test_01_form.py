import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_fill_and_highlight(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Заполнение полей
    wait.until(EC.presence_of_element_located((By.NAME, "first_name"))).send_keys("Иван")
    driver.find_element(By.NAME, 'last_name').send_keys('Петров')
    driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
    driver.find_element(By.NAME, 'email').send_keys('test@skypro.com')
    driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "zip-code").send_keys("12345")  # предполагается, что правильный локатор — zip-code
    
    # Проверка цвета (по классу) у div с id 'zip-code'
    zip_div = driver.find_element(By.ID, "zip-code")
    classes = zip_div.get_attribute("class")
    assert "alert-danger" in classes
    
    # Выбор страны
    country_select = Select(driver.find_element(By.NAME, 'country'))
    country_select.select_by_visible_text('Россия')
    
    # Заполнение работы и компании
    driver.find_element(By.NAME, 'job').send_keys('QA')
    driver.find_element(By.NAME, 'company').send_keys('SkyPro')
    
    # Нажать Submit
    driver.find_element(By.ID, 'submit').click()
    
    # Проверка подсветки поля zip-кода
    zip_field = wait.until(EC.presence_of_element_located((By.NAME, 'zip-code')))
    border_color_zip = zip_field.value_of_css_property('border-color')
    assert border_color_zip in ['rgb(255, 0, 0)', 'red'], \
        f'Цвет границы zip-кода: {border_color_zip}'
    
    # Проверка подсветки других полей (зеленый цвет)
    other_fields_ids = [
        'first_name', 'last_name', 'address', 'email', 
        'phone', 'address', 'city', 'country', 'job', 'company'
    ]
    for field_name in other_fields_ids:
        field = driver.find_element(By.NAME, field_name)
        color = field.value_of_css_property('border-color')
        # ожидание зеленого цвета или другого, в зависимости от UI
        assert color in ['rgb(0, 128, 0)', 'green'], \
            f'Поле {field_name} подсвечено не зеленым, цвет: {color}'
