from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")

close_locator = ".modal-footer"
search_close = driver.find_element(By.CSS_SELECTOR, close_locator)
sleep(2)
search_close.click()
driver.quit()
