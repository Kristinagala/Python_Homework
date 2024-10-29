from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Calc:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def waits_seconds(self, tern):
        input_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        input_field.clear()
        input_field.send_keys(tern)

    def sum(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait(self):
        try:

            WebDriverWait(self._driver, 45, 0.1).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

        except TimeoutException:
            print("Время вышло")

    def sum_resuit(self):
        result_field = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        print(result_field)
        
        return result_field
    
    def close_driver(self):
        self._driver.quit()
