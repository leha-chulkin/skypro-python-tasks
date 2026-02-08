import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Страница товаров интернет-магазина."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы товаров.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        
        # Локаторы товаров
        self.backpack_add_button: Tuple[str, str] = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bolt_tshirt_add_button: Tuple[str, str] = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button: Tuple[str, str] = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button: Tuple[str, str] = (By.CLASS_NAME, "shopping_cart_link")
    
    @allure.step("Добавить рюкзак в корзину")
    def add_backpack_to_cart(self) -> None:
        """Добавить товар 'Sauce Labs Backpack' в корзину."""
        self.click_element(self.backpack_add_button)
    
    @allure.step("Добавить футболку в корзину")
    def add_bolt_tshirt_to_cart(self) -> None:
        """Добавить товар 'Sauce Labs Bolt T-Shirt' в корзину."""
        self.click_element(self.bolt_tshirt_add_button)
    
    @allure.step("Добавить комбинезон в корзину")
    def add_onesie_to_cart(self) -> None:
        """Добавить товар 'Sauce Labs Onesie' в корзину."""
        self.click_element(self.onesie_add_button)
    
    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Перейти на страницу корзины."""
        self.click_element(self.cart_button)
