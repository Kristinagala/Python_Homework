from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

WebDriverWait(driver, 40, 0.1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )
print(driver.find_element(By.CSS_SELECTOR, "p.bg-success").text)
driver.quit()
