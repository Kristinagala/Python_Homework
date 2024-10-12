from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
           )

WebDriverWait(driver, 40, 0.1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape"))
    )

images = driver.find_elements(By.CSS_SELECTOR, "img")
print(len(images))
print(images[2].get_attribute("src"))
driver.quit()
