from base.conftest import init_browser
from pages.login_page import Login_page
from pages.product_page import Product_page

class TestProductPage:
    def test2_cart_icon_is_clickable(self, init_browser):
        driver = init_browser
        lp = Login_page(driver)

        logger = Product_page.get_logger("productPage")  # Use logger from Login_page
        pp = Product_page(driver)  # Instantiate Product_page without passing logger
        logger.info("Starting test2_cart_icon_is_clickable")

        try:
            actual_url = lp.login("standard_user", "secret_sauce").selectProduct().get_actual_url()
            exp_url = "https://www.saucedemo.com/cart.html"
            assert actual_url == exp_url, f"Expected {exp_url}, but got {actual_url}"
            logger.info("Test2 passed: cart icon is clickable.")
        except AssertionError as e:
            logger.error(f"Assertion Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            raise
