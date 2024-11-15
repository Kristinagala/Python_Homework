from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Calc:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def waits_seconds(self, tern: int) -> None:
        """Этот метод устанавливает время ожидания (в секундах), после
        которого будет получен результат арифметических операций"""
        input_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        input_field.clear()
        input_field.send_keys(tern)

    def sum(self) -> None:
        """Этот метод производит сложение чисел 7 и 8"""
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait(self) -> None:
        """Этот метод начинает отсчет времени после которого будет получен
        результат арифметических операций. Если указанное количество времени
        проходит без завершения задачи, в консоль печатается тект исключения"""
        try:

            WebDriverWait(self._driver, 5, 0.1).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

        except TimeoutException:
            print("Время вышло")

    def sum_resuit(self) -> str:
        """Этот метод возвращает результат арифметических операций.
          Результат печатается в консоль"""
        result_field = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        print(result_field)
        
        return result_field
    
    def close_driver(self) -> None:
        """Этот метод закрывает браузер"""
        self._driver.quit()
