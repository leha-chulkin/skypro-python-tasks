import pytest
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestStore:
    """Тесты для интернет-магазина."""
    
    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации WebDriver."""
        driver = webdriver.Chrome()
        yield driver
        driver.quit()
    
    @allure.title("Тест оформления заказа")
    @allure.description("Проверка полного цикла оформления заказа в интернет-магазине")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_store_checkout(self, driver):
        """
        Тестирование полного цикла покупки в интернет-магазине.
        
        Steps:
        1. Авторизация пользователя
        2. Добавление товаров в корзину
        3. Оформление заказа
        4. Проверка итоговой суммы
        """
        # Инициализация страниц
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        with allure.step("Открыть сайт магазина и авторизоваться"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Добавить товары в корзину"):
            products_page.add_backpack_to_cart()
            products_page.add_bolt_tshirt_to_cart()
            products_page.add_onesie_to_cart()
        
        with allure.step("Перейти в корзину и начать оформление"):
            products_page.go_to_cart()
            cart_page.click_checkout()
        
        with allure.step("Заполнить форму оформления заказа"):
            checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
        
        with allure.step("Проверить итоговую сумму заказа"):
            total_amount = checkout_page.get_total_amount()
            assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получено ${total_amount}"
