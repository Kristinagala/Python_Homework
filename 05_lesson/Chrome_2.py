from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")
blue_button_locator = ".btn.btn-primary"
serch_button = driver.find_element(By.CSS_SELECTOR, blue_button_locator)
sleep(3)
serch_button.click()
sleep(3)
