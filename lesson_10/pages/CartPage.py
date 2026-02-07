from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр веб-драйвера
        """
        self._driver = driver
        self._driver.implicitly_wait(4)

    def get_cart_items(self) -> List[str]:
        """
        Получить список товаров в корзине.

        :return: Список названий товаров
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, "cart_list"))
        )

        items = self._driver.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )
        return [item.text for item in items]

    def click_checkout(self) -> None:
        """
        Нажать кнопку оформления заказа.
        """
        checkout_button = self._driver.find_element(By.ID, "checkout")
        checkout_button.click()
