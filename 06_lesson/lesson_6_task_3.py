from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
)

try:
    # Ждём, пока в контейнере появится минимум 4 картинки
    images = WebDriverWait(driver, 20).until(
        lambda d: len(d.find_elements
                      (By.CSS_SELECTOR, '#image-container img')) >= 4
    )

    # Получаем все картинки
    all_images = driver.find_elements(By.CSS_SELECTOR, '#image-container img')

    # Берём третью картинку и выводим её src
    third_img_src = all_images[2].get_attribute('src')
    print(third_img_src)
finally:
    driver.quit()
