import logging
from logging.handlers import RotatingFileHandler
from selenium.webdriver.common.by import By
from base.base import Base
from pages.product_page import Product_page


class Login_page(Base):
    logger = None
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Password']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")

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
        self.logger = Login_page.get_logger("loginPage")

    def login(self, username, password):
        try:
            self.enter_text(self.USERNAME_FIELD, username, "USERNAME_FIELD")
            self.logger.info(f"'{username}' passed to USERNAME_FIELD")
            self.enter_text(self.PASSWORD_FIELD, password, "PASSWORD_FIELD")
            self.logger.info(f"'{password}' passed to PASSWORD_FIELD")
            self.click_element(self.SUBMIT_BUTTON, "SUBMIT_BTN")
            self.logger.info("Clicked on SUBMIT_BTN")
            return Product_page(self.driver)
        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            raise
