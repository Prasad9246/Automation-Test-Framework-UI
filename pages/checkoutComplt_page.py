
class CheckoutComplete_page:
    def __init__(self, driver):
        self.driver = driver

    def get_actual_url(self):
        return self.driver.current_url