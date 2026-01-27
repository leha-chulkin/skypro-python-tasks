from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        
        # Локаторы товаров
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bolt_tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
    
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack_add_button).click()
    
    def add_bolt_tshirt_to_cart(self):
        self.driver.find_element(*self.bolt_tshirt_add_button).click()
    
    def add_onesie_to_cart(self):
        self.driver.find_element(*self.onesie_add_button).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
