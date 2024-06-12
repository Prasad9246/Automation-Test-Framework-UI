import pytest
from base.conftest import init_browser
from pages.Info_page import Info_page
from pages.login_page import Login_page
from base.conftest import test_data

class TestInfoPage:
    def test4_textfield_and_Submit_Btn(self, init_browser, test_data):
        username, password, firstname, lastname, postalcode = test_data
        driver = init_browser
        lp = Login_page(driver)
        logger = Info_page.get_logger("InfoPage")
        logger.info("Starting test4_textfield_and_Submit_Btn")

        try:
            actual_url = lp.login(username, password).selectProduct().verifyYourCartPage().verifyInfo_page(firstname, lastname, postalcode).get_actual_url()
            exp_url = "https://www.saucedemo.com/checkout-step-two.html"
            assert actual_url == exp_url, f"Expected {exp_url}, but got {actual_url}"
            logger.info("Test4 passed: Text fields and Submit button are clickable.")
        except AssertionError as e:
            logger.error(f"Assertion Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            raise