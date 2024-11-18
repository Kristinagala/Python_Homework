import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from form import Form

@allure.epic("Автотесты")

@allure.title("Автотест на заполнение формы")
@allure.description("Тест проверяет, что поле Zip code подсвечено красным, а остальные поля подсвечены зеленым")
@allure.feature("Backlight")
@allure.severity("critical")
def test_form():
    with allure.step("Подключиться к браузеру"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        with allure.step("Передать браузер в класс"):
            form = Form(browser)
    with allure.step("Заполнить поля параметрами"):
        form.fill_out("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", +79858999987, "Москва", "Россия", "QA", "SkyPro")
    with allure.step("Идентифицировать цвет поля Zip code"):
        zс_bg_color = form.check_red_field()
    with allure.step("Идентифицировать цвет остальных полей"):
        bg_color = form.check_green_field()
    with allure.step("Проверить, что цвет поля Zip code подсвечено красным"):
        assert zс_bg_color == "rgba(248, 215, 218, 1)", "Поле не подсвечено красным"
    with allure.step("Проверить, что цвет остальных полей подсвечено зеленым"):
        assert bg_color == "rgba(209, 231, 221, 1)", "Поле не подсвечено зеленым"
    with allure.step("Закрыть браузер"):
        form.close_driver()
