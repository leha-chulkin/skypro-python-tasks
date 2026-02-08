import pytest
import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для калькулятора с задержкой выполнения."""
    
    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации WebDriver."""
        driver = webdriver.Chrome()
        yield driver
        driver.quit()
    
    @allure.title("Тест сложения с задержкой")
    @allure.description("Проверка корректности сложения чисел с задержкой выполнения операций")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_calculator_addition(self, driver):
        """
        Тестирование операции сложения в калькуляторе с задержкой.
        
        Steps:
        1. Открыть страницу калькулятора
        2. Установить задержку 45 секунд
        3. Выполнить операцию 7 + 8
        4. Проверить результат равен 15
        """
        calculator_page = CalculatorPage(driver)
        
        with allure.step("Открыть страницу калькулятора"):
            calculator_page.open()
        
        with allure.step("Установить задержку выполнения операций"):
            calculator_page.set_delay(45)
        
        with allure.step("Выполнить операцию сложения 7 + 8"):
            calculator_page.click_button_7()
            calculator_page.click_plus()
            calculator_page.click_button_8()
            calculator_page.click_equals()
        
        with allure.step("Проверить результат вычисления"):
            result = calculator_page.get_result()
            assert result == "15", f"Ожидался результат '15', но получено '{result}'"
