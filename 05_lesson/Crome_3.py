from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")

button_locator = ".btn-primary"
search_button = driver.find_element(By.CSS_SELECTOR, button_locator)
search_button.click()
sleep(3)
alert = driver.switch_to.alert
alert.accept()
sleep(3)
