from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from calc import Calc


def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc = Calc(browser)
    calc.waits_seconds(45)
    calc.sum()
    calc.wait()
    result_field = calc.sum_resuit()
    assert result_field == "15", "Результат не равен 15"
    calc.close_driver()
