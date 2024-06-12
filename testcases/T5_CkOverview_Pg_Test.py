from pages.checkoutOverview_page import CheckoutOverview_page
from pages.login_page import Login_page
from base.conftest import init_browser
import logging


class Test_CheckoutOverview_page:
    def test5_Finish_Btn_IsClickable(self, init_browser):
        driver = init_browser
        lp = Login_page(driver)
        logger = CheckoutOverview_page.get_logger("OverviewPage")
        logger.info("Starting test5_Finish_Btn_IsClickable")

        try:
            actual_url = lp.login("standard_user", "secret_sauce").selectProduct().verifyYourCartPage().verifyInfo_page("PK", "KD", "789").verify_checkout_Overview_page().get_actual_url()
            exp_url = "https://www.saucedemo.com/checkout-complete.html"
            assert actual_url == exp_url, f"Expected {exp_url}, but got {actual_url}"
            logger.info("Test5 passed: Finish button is clickable.")
        except AssertionError as e:
            logger.error(f"Assertion Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            raise