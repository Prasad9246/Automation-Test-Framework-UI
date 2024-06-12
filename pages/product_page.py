from selenium.webdriver.common.by import By
import logging
from logging.handlers import RotatingFileHandler
from base.base import Base
from pages.yourCart_page import YourCart_page

class Product_page(Base):
    logger = None
    PRODUCT_TO_SELECT = (By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")

    @classmethod
    def get_logger(cls, name, log_dir='logs'):
        if cls.logger is None:
            cls.logger = logging.getLogger(name)
            cls.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            log_file = f"{log_dir}/{name}.log"
            file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            cls.logger.addHandler(file_handler)
        return cls.logger

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Product_page.get_logger("productPage")

    def get_actual_url(self):
        return self.driver.current_url

    def selectProduct(self):
        try:
            self.click_element(self.PRODUCT_TO_SELECT, "PRODUCT_TO_SELECT")
            self.logger.info("Clicked on PRODUCT")
            self.click_element(self.CART_ICON, "CART_ICON")
            self.logger.info("Clicked on cart icon")
            return YourCart_page(self.driver)
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")
            raise
