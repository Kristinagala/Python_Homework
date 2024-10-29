from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from mane_page import MainPage
from products_page import ProductsPage
from you_cart_page import YouCart
from information_page import Information
from price_total import PriceTotal


def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.get()
    main_page.authorization("standard_user", "secret_sauce")
    product = ProductsPage(browser)
    product.add_to_cart()
    cart = YouCart(browser)
    cart.checkout()
    information = Information(browser)
    information.fill_out_the_forms("Harry", "Potter", "12345")
    total_price = PriceTotal(browser)
    total = total_price.checkout_price()
    assert total == "Total: $58.29", "Итоговая сумма не равна $58.29"
    total_price.close_browser()
