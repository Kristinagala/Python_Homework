from selenium.webdriver.common.by import By


class Form:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def fill_out(self, first_name, last_name, address, e_mail, phone, city, country, position, company):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(e_mail)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(position)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(company)
        self._driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

    def check_red_field(self):
        Zip_code = self._driver.find_element(By.CSS_SELECTOR, "#zip-code")
        zс_bg_color = Zip_code.value_of_css_property("background-color")

        return zс_bg_color
    
    def check_green_field(self):
        fields = self._driver.find_elements(By.CSS_SELECTOR, ".alert-success")
        for field in fields:
            bg_color = field.value_of_css_property("background-color")

        return bg_color
    
    def close_driver(self):
        self._driver.quit()
