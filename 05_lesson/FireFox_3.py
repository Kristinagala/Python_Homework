from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

username_locator = "#username"
search_username = driver.find_element(By.CSS_SELECTOR, username_locator)
search_username.send_keys("tomsmith")

password_locator = "#password"
search_password = driver.find_element(By.CSS_SELECTOR, password_locator)
search_password.send_keys("SuperSecretPassword!")

login_locator = "i.fa.fa-2x.fa-sign-in"
search_login = driver.find_element(By.CSS_SELECTOR, login_locator)
search_login.click()

sleep(5)
driver.quit()
