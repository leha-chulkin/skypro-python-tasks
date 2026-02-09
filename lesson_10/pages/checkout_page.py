import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Страница оформления заказа интернет-магазина."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        
        # Локаторы формы
        self.first_name_input: Tuple[str, str] = (By.ID, "first-name")
        self.last_name_input: Tuple[str, str] = (By.ID, "last-name")
        self.postal_code_input: Tuple[str, str] = (By.ID, "postal-code")
        self.continue_button: Tuple[str, str] = (By.ID, "continue")
        self.total_label: Tuple[str, str] = (By.CLASS_NAME, "summary_total_label")
        self.finish_button: Tuple[str, str] = (By.ID, "finish")
    
    @allure.step("Заполнить форму оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнить форму данными для оформления заказа.
        
        Args:
            first_name: Имя
            last_name: Фамилия
            postal_code: Почтовый индекс
        """
        self.enter_text(self.first_name_input, first_name)
        self.enter_text(self.last_name_input, last_name)
        self.enter_text(self.postal_code_input, postal_code)
        self.click_element(self.continue_button)
    
    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получить итоговую сумму заказа.
        
        Returns:
            str: Сумма заказа без символа валюты
        """
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(EC.visibility_of_element_located(self.total_label))
        total_text = total_element.text
        return total_text.replace("Total: $", "")
    
    @allure.step("Завершить оформление заказа")
    def finish_checkout(self) -> None:
        """Завершить оформление заказа."""
        self.click_element(self.finish_button)
