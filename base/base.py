# base/base.py
from logging import Logger

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class Base:
    def __init__(self, driver):
        self.driver = driver
        # self.logger = Logger.get_logger(__name__)

    def click_element(self, locator, FIELD):
        try:
           # self.logger.info(f"Waiting for element: {FIELD} to be clickable")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            ).click()
            # self.logger.info(f"Clicked element with locator: {locator}")
        except Exception as e:
            # self.logger.error(f"Error clicking element with locator {locator}: {e}")
            raise

    def enter_text(self, locator, text, FIELD):
        try:
            #self.logger.info(f"Waiting for element: {FIELD} to be visible")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            ).send_keys(text)
            # self.logger.info(f"Entered text '{text}' into element with locator: {locator}")
        except Exception as e:
            # self.logger.error(f"Error entering text '{text}' into element with locator {locator}: {e}")
            raise
