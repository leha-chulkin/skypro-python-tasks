import ssl
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os
import certifi

from shop.AuthorizationPage import AuthorizationPage
from shop.MainPage import MainPage
from shop.CartPage import CartPage
from shop.Order import Order

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['SSL_CERT_FILE'] = certifi.where()
ssl._create_default_https_context = ssl._create_unverified_context


@allure.epic("Магазин")
@allure.feature("Оформление заказа")
@allure.severity("critical")
class TestShop:

    @allure.title("Полный цикл оформления заказа")
    @allure.description("Тест проверяет полный процесс: авторизация, добавление товаров, оформление заказа")
    @allure.story("Пользовательский сценарий покупки")
    def test_shop(self):
        with allure.step("Инициализация Firefox драйвера"):
            options = webdriver.FirefoxOptions()
            options.set_preference('network.http.use-ssl', False)
            options.set_preference('network.http.ssl-force-insecure', True)

            browser = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )

        try:
            with allure.step("Авторизация пользователя"):
                login = AuthorizationPage(browser)
                login.login_account('standard_user', 'secret_sauce')

            with allure.step("Добавление товаров в корзину на главной странице"):
                main_page = MainPage(browser)
                added_products = main_page.add_products()

            with allure.step("Переход в корзину"):
                main_page.go_to_cart()

            with allure.step("Проверка товаров в корзине"):
                cart_page = CartPage(browser)
                cart_items = cart_page.get_cart_items()

                with allure.step("Проверка соответствия добавленных и отображаемых товаров"):
                    assert set(cart_items) == set(added_products)

            with allure.step("Переход к оформлению заказа"):
                cart_page.click_checkout()

            with allure.step("Заполнение информации для доставки"):
                order = Order(browser)
                order.making_in_order('Иван', 'Иванов', '123')

            with allure.step("Проверка итоговой суммы"):
                total_text = order.summary_amount()
                total_amount = total_text.split("$")[1]

                with allure.step("Проверка что итоговая сумма равна 58.29"):
                    assert total_amount == "58.29"

        finally:
            with allure.step("Закрытие браузера"):
                browser.close()
