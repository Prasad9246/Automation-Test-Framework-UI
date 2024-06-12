from base.conftest import init_browser
from pages.login_page import Login_page
from base.conftest import test_data


class TestLogin:

    def test1_Login_Btn_IsClickable(self, init_browser, test_data):
        username, password, firstname, lastname, postalcode = test_data
        driver = init_browser
        login_page = Login_page(driver)

        logger = Login_page.get_logger("loginPage")
        logger.info("Starting test1_Login_Btn_IsClickable")

        try:
            actual_url = login_page.login(username, password).get_actual_url()
            exp_url = "https://www.saucedemo.com/inventory.html"
            assert actual_url == exp_url, f"Expected {
                exp_url}, but got {actual_url}"
            logger.info("Test1 passed: Login button is clickable.")
        except AssertionError as e:
            logger.error(f"Assertion Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            raise
