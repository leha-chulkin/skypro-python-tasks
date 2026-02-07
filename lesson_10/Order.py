from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class Order:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр веб-драйвера
        """
        self._driver = driver

    def making_in_order(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнить информацию для оформления заказа.

        :param first_name: Имя покупателя
        :param last_name: Фамилия покупателя
        :param postal_code: Почтовый индекс
        """
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        continue_button = self._driver.find_element(By.ID, "continue")
        continue_button.click()

    def summary_amount(self) -> str:
        """
        Получить итоговую сумму заказа.

        :return: Текст с итоговой суммой
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, "summary_total_label"))
        )

        total_element = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        total_text = total_element.text

        return total_text
