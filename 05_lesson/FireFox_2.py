from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")

input_locator = "input"
search_input = driver.find_element(By.CSS_SELECTOR, input_locator)
search_input.send_keys(1000)
sleep(2)

search_input.clear()
search_input.send_keys(999)
sleep(2)
driver.quit()
