import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """Общая фикстура для конфигурации браузера.
    
    Returns:
        WebDriver: Экземпляр веб-драйвера.
    """
    # Общая конфигурация браузера
    pass


@pytest.fixture(scope="function")
def chrome_driver():
    """Фикстура для создания драйвера Chrome.
    
    Yields:
        WebDriver: Экземпляр Chrome WebDriver.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def firefox_driver():
    """Фикстура для создания драйвера Firefox.
    
    Yields:
        WebDriver: Экземпляр Firefox WebDriver.
    """
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
