from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        
        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
    
    def open(self):
        self.driver.get(self.url)
    
    def set_delay(self, delay_value):
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(str(delay_value))
    
    def click_button_7(self):
        self.driver.find_element(*self.button_7).click()
    
    def click_button_8(self):
        self.driver.find_element(*self.button_8).click()
    
    def click_plus(self):
        self.driver.find_element(*self.button_plus).click()
    
    def click_equals(self):
        self.driver.find_element(*self.button_equals).click()
    
    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        result_element = wait.until(
            EC.text_to_be_present_in_element(self.result_field, "15")
        )
        return self.driver.find_element(*self.result_field).text
