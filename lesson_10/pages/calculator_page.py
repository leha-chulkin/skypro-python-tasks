import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple
from pages.base_page import BasePage


class CalculatorPage(BasePage):
    """Страница калькулятора с задержкой выполнения операций."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        
        # Локаторы
        self.delay_input: Tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        self.result_field: Tuple[str, str] = (By.CSS_SELECTOR, ".screen")
        self.button_7: Tuple[str, str] = (By.XPATH, "//span[text()='7']")
        self.button_8: Tuple[str, str] = (By.XPATH, "//span[text()='8']")
        self.button_plus: Tuple[str, str] = (By.XPATH, "//span[text()='+']")
        self.button_equals: Tuple[str, str] = (By.XPATH, "//span[text()='=']")
    
    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открыть страницу калькулятора."""
        self.driver.get(self.url)
    
    @allure.step("Установить задержку: {delay_value} секунд")
    def set_delay(self, delay_value: int) -> None:
        """
        Установить значение задержки выполнения операций.
        
        Args:
            delay_value: Значение задержки в секундах
        """
        self.enter_text(self.delay_input, str(delay_value))
    
    @allure.step("Нажать кнопку '7'")
    def click_button_7(self) -> None:
        """Нажать кнопку с цифрой 7."""
        self.click_element(self.button_7)
    
    @allure.step("Нажать кнопку '8'")
    def click_button_8(self) -> None:
        """Нажать кнопку с цифрой 8."""
        self.click_element(self.button_8)
    
    @allure.step("Нажать кнопку '+'")
    def click_plus(self) -> None:
        """Нажать кнопку сложения."""
        self.click_element(self.button_plus)
    
    @allure.step("Нажать кнопку '='")
    def click_equals(self) -> None:
        """Нажать кнопку вычисления результата."""
        self.click_element(self.button_equals)
    
    @allure.step("Получить результат вычисления")
    def get_result(self, timeout: int = 50) -> str:
        """
        Получить результат вычисления с ожиданием.
        
        Args:
            timeout: Максимальное время ожидания в секундах
            
        Returns:
            str: Текст результата
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.result_field, "15"))
        element = self.find_element(self.result_field)
        return element.text
