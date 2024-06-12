import logging
from logging.handlers import RotatingFileHandler
from selenium.webdriver.common.by import By
from base.base import Base
from pages.checkoutComplt_page import CheckoutComplete_page


class CheckoutOverview_page(Base):
    FINISH_BTN = (By.XPATH, "//button[@name='finish']")
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
        self.logger = CheckoutOverview_page.get_logger("OverviewPage")

    def get_actual_url(self):
        return self.driver.current_url

    def verify_checkout_Overview_page(self):
        try:
            self.click_element(self.FINISH_BTN, "FINISH_BTN")
            self.logger.info("Clicked on FINISH_BTN")
            return CheckoutComplete_page(self.driver)
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")
            raise
