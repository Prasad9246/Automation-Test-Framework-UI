import logging
from logging.handlers import RotatingFileHandler
from selenium.webdriver.common.by import By
from base.base import Base
from pages.checkoutOverview_page import CheckoutOverview_page

class Info_page(Base):
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    POSTAL_CODE = (By.XPATH, "//input[@placeholder='Zip/Postal Code']")
    SUBMIT_BTN = (By.XPATH, "//input[@type='submit']")
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
        self.logger = Info_page.get_logger("InfoPage")

    def get_actual_url(self):
        return self.driver.current_url

    def verifyInfo_page(self, firstname, lastname, postalcode):
        try:
            self.enter_text(self.FIRST_NAME, firstname,"FIRST_NAME")
            self.logger.info(f"'{firstname}' is passed to FIRST_NAME field")
            self.enter_text(self.LAST_NAME, lastname,"LAST_NAME")
            self.logger.info(f"'{lastname}' is passed to LAST_NAME text field")
            self.enter_text(self.POSTAL_CODE, postalcode,"POSTAL CODE FIELD")
            self.logger.info(f"'{postalcode}' passed to POSTAL_CODE text field")
            self.click_element(self.SUBMIT_BTN,"SUBMIT_BTN")
            self.logger.info("Clicked on SUBMIT_BTN")
            return CheckoutOverview_page(self.driver)
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")
            raise