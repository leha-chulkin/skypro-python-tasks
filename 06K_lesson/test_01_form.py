from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Создаем экземпляр драйвера
driver = webdriver.Edge()
wait = WebDriverWait(driver, 15)  # Увеличьте тайм-аут при необходимости

# Корректный URL без лишних пробелов
url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"  # Проверьте актуальность URL

driver.get(url)

# Сопоставление имен полей (подтвердите в HTML документах)
field_mapping = {
    "First name": "first-name",
    "Last name": "last-name",
    "Address": "address",
    "Email": "e-mail",
    "Phone": "phone",
    "Zip code": "zip-code",
    "City": "city",
    "Country": "country",
    "Job position": "job-position",
    "Company": "company",
}

# Данные для заполнения
data_to_fill = {
    "First name": "Иван",
    "Last name": "Иванов",
    "Address": "Ленина, 55-3",
    "Email": "test@skypro.com",
    "Phone": "+7985899998787",
    "Zip code": "",
    "City": "Москва",
    "Country": "Россия",
    "Job position": "QA",
    "Company": "SkyPro",
}

# Заполнение формы
for label, name_attr in field_mapping.items():
    try:
        element = wait.until(EC.element_to_be_clickable((By.NAME, name_attr)))
        element.clear()
        element.send_keys(data_to_fill[label])
        print(f"Поле '{label}' заполнено.")
    except Exception as e:
        print(f"Ошибка при заполнении поля '{label}': {e}")

# Найти кнопку отправки формы и кликнуть
try:
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()
    print("Форма отправлена.")
except Exception as e:
    print(f"Ошибка при отправке формы: {e}")

# Ожидание для проверки результата (можно заменить на конкретное ожидаемое состояние)
time.sleep(3)

driver.quit()
