import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

class TestCalculator:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()
    
    def test_calculator_addition(self, driver):
        calculator_page = CalculatorPage(driver)
        
        # Открыть страницу калькулятора
        calculator_page.open()
        
        # Ввести значение 45 в поле задержки
        calculator_page.set_delay(45)
        
        # Нажать кнопки: 7, +, 8, =
        calculator_page.click_button_7()
        calculator_page.click_plus()
        calculator_page.click_button_8()
        calculator_page.click_equals()
        
        # Проверить, что в окне отобразится результат 15 через 45 секунд
        result = calculator_page.get_result()
        assert result == "15", f"Ожидался результат '15', но получено '{result}'"
