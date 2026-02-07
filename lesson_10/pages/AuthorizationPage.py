from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthorizationPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: Экземпляр веб-драйвера
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def login_account(self, username: str, password: str) -> None:
        """
        Выполнить авторизацию пользователя.

        :param username: Имя пользователя
        :param password: Пароль
        :return: None
        """
        self._driver.find_element(By.ID, "user-name").send_keys(username)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()
