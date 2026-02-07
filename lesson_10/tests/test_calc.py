import ssl
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import certifi

from calc.CalculatorPage import CalculatorPage

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['SSL_CERT_FILE'] = certifi.where()
ssl._create_default_https_context = ssl._create_unverified_context


@allure.epic("Калькулятор")
@allure.feature("Медленные вычисления")
@allure.severity("normal")
class TestCalculator:

    @allure.title("Тест медленного калькулятора")
    @allure.description("Проверка вычисления 7 + 8 с задержкой 45 секунд")
    @allure.story("Выполнение операции сложения")
    def test_slow_calculator(self):
        with allure.step("Инициализация драйвера"):
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')

            browser = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )

        try:
            with allure.step("Создание объекта страницы калькулятора"):
                calculator_page = CalculatorPage(browser)

            with allure.step("Выполнение вычисления 7 + 8 с задержкой 45 секунд"):
                calculator_page.calculate_7_plus_8(delay_seconds=45)

            with allure.step("Ожидание результата '15'"):
                calculator_page.wait_for_result("15", timeout=50)

            with allure.step("Получение финального результата"):
                final_result = calculator_page.get_result()

            with allure.step("Проверка результата"):
                assert final_result == "15"

        finally:
            with allure.step("Закрытие браузера"):
                browser.quit()
