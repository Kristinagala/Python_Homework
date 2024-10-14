from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)


Username = driver.find_element(By.CSS_SELECTOR, "#user-name")
Username.send_keys("standard_user")
Password = driver.find_element(By.CSS_SELECTOR, "#password")
Password.send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()


driver.find_element(By.CSS_SELECTOR,
                    "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR,
                    "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR,
                    "#add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()


driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Harry")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Potter")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, "#continue").click()

total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
print(total)
assert total == "Total: $58.29", "Итоговая сумма не равна $58.29"
driver.quit()
