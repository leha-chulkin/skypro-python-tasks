from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: Экземпляр веб-драйвера
        """
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self.waiter = WebDriverWait(driver, 50)

    def set_delay(self, delay_seconds: int) -> 'CalculatorPage':
        """
        Установить задержку вычислений.

        :param delay_seconds: Задержка в секундах
        :return: Текущий экземпляр страницы (для цепочки вызовов)
        """
        self.waiter.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
        return self

    def click_button(self, button_text: str) -> 'CalculatorPage':
        """
        Нажать кнопку по тексту.

        :param button_text: Текст на кнопке
        :return: Текущий экземпляр страницы
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        )
        button.click()
        return self

    def press_7(self) -> 'CalculatorPage':
        """
        Нажать кнопку '7'.

        :return: Текущий экземпляр страницы
        """
        return self.click_button("7")

    def press_8(self) -> 'CalculatorPage':
        """
        Нажать кнопку '8'.

        :return: Текущий экземпляр страницы
        """
        return self.click_button("8")

    def press_plus(self) -> 'CalculatorPage':
        """
        Нажать кнопку '+'.

        :return: Текущий экземпляр страницы
        """
        return self.click_button("+")

    def press_equals(self) -> 'CalculatorPage':
        """
        Нажать кнопку '='.

        :return: Текущий экземпляр страницы
        """
        return self.click_button("=")

    def get_result(self) -> str:
        """
        Получить текущий результат с экрана калькулятора.

        :return: Текст результата
        """
        result_element = self.driver.find_element(By.CLASS_NAME, "screen")
        return result_element.text

    def wait_for_result(self, expected_result: str, timeout: int = 50) -> bool:
        """
        Дождаться появления ожидаемого результата.

        :param expected_result: Ожидаемый результат
        :param timeout: Время ожидания в секундах
        :return: True если результат появился, False если время вышло
        """
        waiter = WebDriverWait(self.driver, timeout)

        try:
            waiter.until(
                lambda d: d.find_element(
                    By.CLASS_NAME, "screen"
                ).text == str(expected_result)
            )
            return True
        except Exception:
            return False

    def calculate_7_plus_8(self, delay_seconds: int = 45) -> 'CalculatorPage':
        """
        Выполнить вычисление 7 + 8 с указанной задержкой.

        :param delay_seconds: Задержка вычислений в секундах
        :return: Текущий экземпляр страницы
        """
        self.set_delay(delay_seconds)
        self.press_7()
        self.press_plus()
        self.press_8()
        self.press_equals()
        return self
