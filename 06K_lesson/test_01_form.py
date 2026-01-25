from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Создаём экземпляр драйвера
driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

# Ваш URL с формой
url = " https://bonigarcia.dev/selenium-webdriver-java/data-types.html"  # Замените на фактический URL

driver.get(url)

# Правильное соответствие полей
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

# Пример данных для заполнения
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

# Заполняем поля
for label, name_attr in field_mapping.items():
    try:
        # Ищем элемент по имени
        element = wait.until(EC.presence_of_element_located((By.NAME, name_attr)))
        # Заполняем его значением из данных
        element.clear()  # очистка поля
        element.send_keys(data_to_fill[label])
        print(f"Заполнено поле '{label}'")
    except Exception as e:
        print(f"Не удалось найти или заполнить поле '{label}': {e}")

# После заполнения, ищем кнопку "Submit" и кликаем по ней
try:
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()
    print("Форма отправлена.")
except Exception as e:
    print(f"Ошибка при отправке формы: {e}")

# Ждём немного, чтобы убедиться, что форма отправилась (опционально)
time.sleep(3)

# Закрываем драйвер
driver.quit()
