import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple


class BasePage:
    """Базовый класс для всех страниц приложения."""
    
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация базовой страницы.
        
        Args:
            driver: Экземпляр WebDriver
            timeout: Таймаут для явных ожиданий в секундах
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        """
        Найти элемент на странице с ожиданием.
        
        Args:
            locator: Кортеж (By, value) для поиска элемента
            timeout: Время ожидания в секундах
            
        Returns:
            WebElement: Найденный элемент
        """
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator: Tuple[str, str]) -> None:
        """
        Кликнуть по указанному элементу.
        
        Args:
            locator: Кортеж (By, value) для поиска элемента
        """
        element = self.find_element(locator)
        element.click()
    
    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def enter_text(self, locator: Tuple[str, str], text: str) -> None:
        """
        Ввести текст в поле ввода.
        
        Args:
            locator: Кортеж (By, value) для поиска элемента
            text: Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
