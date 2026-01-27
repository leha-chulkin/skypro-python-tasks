import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestStore:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Firefox()
        yield driver
        driver.quit()
    
    def test_store_checkout(self, driver):
        # Инициализация страниц
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        # Открыть сайт магазина
        login_page.open()
        
        # Авторизоваться как пользователь standard_user
        login_page.login("standard_user", "secret_sauce")
        
        # Добавить товары в корзину
        products_page.add_backpack_to_cart()
        products_page.add_bolt_tshirt_to_cart()
        products_page.add_onesie_to_cart()
        
        # Перейти в корзину
        products_page.go_to_cart()
        
        # Нажать кнопку Checkout
        cart_page.click_checkout()
        
        # Заполнить форму данными
        checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
        
        # Прочитать итоговую стоимость
        total_amount = checkout_page.get_total_amount()
        
        # Проверить, что итоговая сумма равна $58.29
        assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получено ${total_amount}"
