import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации интернет-магазина."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
        
        # Локаторы
        self.username_input: Tuple[str, str] = (By.ID, "user-name")
        self.password_input: Tuple[str, str] = (By.ID, "password")
        self.login_button: Tuple[str, str] = (By.ID, "login-button")
    
    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """Открыть страницу авторизации."""
        self.driver.get(self.url)
    
    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполнить авторизацию.
        
        Args:
            username: Имя пользователя
            password: Пароль
        """
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click_element(self.login_button)
