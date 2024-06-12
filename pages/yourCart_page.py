import logging
from logging.handlers import RotatingFileHandler
from selenium.webdriver.common.by import By
from base.base import Base
from pages.Info_page import Info_page

class YourCart_page(Base):
    CHECKOUT_BTN = (By.XPATH, "//button[@name='checkout']")
    logger = None  # Class-level logger

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
        self.logger = YourCart_page.get_logger("YourCart")  # Using class-level logger

    def get_actual_url(self):
        return self.driver.current_url

    def verifyYourCartPage(self):
        try:
            self.click_element(self.CHECKOUT_BTN, "CHECKOUT_BTN")
            self.logger.info("Clicked on CHECKOUT_BTN")
            return Info_page(self.driver)
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")
            raise
