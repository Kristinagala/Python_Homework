import allure
from selenium.webdriver.common.by import By


class YouCart:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Переход на следущую страницу")
    def checkout(self) -> None:
        """Этот метод нажимает на кнопку "Checkout" для перехода на
        следующую страницу"""
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
