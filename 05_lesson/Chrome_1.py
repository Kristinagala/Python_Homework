from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
add_elevent_locator = "button[onclick='addElement()']"
add_elevent_button = driver.find_element(By.CSS_SELECTOR, add_elevent_locator)
for х in range(5):
    add_elevent_button.click()
sleep(3)

delete_buttons_locator = ".added-manually"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, delete_buttons_locator)
print(len(delete_buttons))
