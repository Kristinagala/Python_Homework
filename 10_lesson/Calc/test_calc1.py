import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from calc import Calc

@allure.epic("Автотесты")

@allure.title("Автотест на калькулятор")
@allure.description("Тест проверяет, что в окне отобразится результат 15 через 5 секунд")
@allure.feature("Wait")
@allure.severity("critical")
def test_calc():
    with allure.step("Подключиться к браузеру"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        with allure.step("Передать браузер в класс"):
            calc = Calc(browser)
    with allure.step("Установить время ожидания"):
        calc.waits_seconds(5)
    with allure.step("Произвести сложение"):
        calc.sum()
    with allure.step("Отсчет времени ожидания"):
        calc.wait()
    with allure.step("Получить результат сложения"):
        result_field = calc.sum_resuit()
    with allure.step("Сравнить результат с ожидаемым"):
        assert result_field == "15", "Результат не равен 15"
    with allure.step("Закрыть браузер"):
        calc.close_driver()
