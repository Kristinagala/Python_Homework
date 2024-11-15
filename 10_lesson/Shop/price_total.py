import allure
from selenium.webdriver.common.by import By


class PriceTotal:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Получить сумму всх товаров в корзине")
    def checkout_price(self) -> str:
        """Этот метод возвращает сумму всех добавленных в корзину товаров"""
        total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(total)

        return total

    @allure.step("Закрыть браузер")
    def close_browser(self) -> None:
        """Этот метод закрывает браузер"""
        self._driver.quit()
