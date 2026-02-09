import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple, List
from pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины интернет-магазина."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        
        # Локаторы
        self.checkout_button: Tuple[str, str] = (By.ID, "checkout")
        self.cart_items: Tuple[str, str] = (By.CLASS_NAME, "cart_item")
    
    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """Перейти к оформлению заказа."""
        self.click_element(self.checkout_button)
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Получить количество товаров в корзине.
        
        Returns:
            int: Количество товаров
        """
        elements = self.driver.find_elements(*self.cart_items)
        return len(elements)
