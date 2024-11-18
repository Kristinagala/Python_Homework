import allure
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открыть браузер")
    def get(self) -> None:
        """Этот метод открывает и настраивает браузер"""
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)

    @allure.step("Авторизоваться")
    def authorization(self, user_name: str, password: str) -> None:
        """Этот метод авторизует пользователя"""
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
