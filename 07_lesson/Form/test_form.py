from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from form import Form


def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form = Form(browser)
    form.fill_out("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+79858999987", "Москва", "Россия", "QA", "SkyPro")
    zс_bg_color = form.check_red_field()
    bg_color = form.check_green_field()
    assert zс_bg_color == "rgba(248, 215, 218, 1)", "Поле не подсвечено красным"
    assert bg_color == "rgba(209, 231, 221, 1)", "Поле не подсвечено зеленым"
    form.close_driver()
