from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

input_field = driver.find_element(By.CSS_SELECTOR, "#delay")
input_field.clear()
input_field.send_keys(45)

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

try:

    WebDriverWait(driver, 45, 0.1).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

except TimeoutException:
    print("Время вышло")

result_field = driver.find_element(By.CSS_SELECTOR, ".screen")
result = result_field.text
print(result)
assert result == "15", "Результат не равен 15"
driver.quit()
