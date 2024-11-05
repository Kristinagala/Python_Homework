from selenium.webdriver.common.by import By


class PriceTotal:

    def __init__(self, driver):
        self._driver = driver

    def checkout_price(self):
        total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(total)

        return total

    def close_browser(self):
        self._driver.quit()
