import pytest
from base.conftest import init_browser
from pages.login_page import Login_page
from pages.yourCart_page import YourCart_page

class TestCartPage:
    def test3_Checkout_Btn(self, init_browser):
        driver = init_browser
        lp = Login_page(driver)
        logger = YourCart_page.get_logger("YourCart")
        logger.info("Starting test3_Checkout_Btn")

        try:
            actual_url = lp.login("standard_user", "secret_sauce").selectProduct().verifyYourCartPage().get_actual_url()
            exp_url = "https://www.saucedemo.com/checkout-step-one.html"
            assert actual_url == exp_url, f"Expected {exp_url}, but got {actual_url}"
            logger.info("Test3 passed: Checkout button is clickable.")
        except AssertionError as e:
            logger.error(f"Assertion Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            raise