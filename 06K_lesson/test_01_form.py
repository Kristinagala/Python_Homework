from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.implicitly_wait(10)

First_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
First_name.send_keys("Иван")
last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
last_name.send_keys("Петров")
Address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
Address.send_keys("Ленина, 55-3")
Email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
Email.send_keys("test@skypro.com")
Phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
Phone_number.send_keys("+7985899998787")
City = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
City.send_keys("Москва")
Country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
Country.send_keys("Россия")
Job_position = driver.find_element(By.CSS_SELECTOR,
                                   "input[name='job-position']")
Job_position.send_keys("QA")
Company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
Company.send_keys("SkyPro")

Submit = driver.find_element(By.CSS_SELECTOR,
                             "button.btn.btn-outline-primary.mt-3")
Submit.click()

Zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
zс_bg_color = Zip_code.value_of_css_property("background-color")

print("Цвет фона поля Zip-code:", zс_bg_color)
assert zс_bg_color == "rgba(248, 215, 218, 1)", "Поле не подсвечено красным"

fields = driver.find_elements(By.CSS_SELECTOR, ".alert-success")

for field in fields:
    bg_color = field.value_of_css_property("background-color")
    print("Цвет фона поля", bg_color)

assert bg_color == "rgba(209, 231, 221, 1)", "Поле не подсвечено зеленым"
driver.quit()
