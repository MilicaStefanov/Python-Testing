import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/shone/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, Name, LinkText

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# how to handle static dropdowns?

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")

# Xpath, //tagname[@attribute = 'value'] -> //input[@type = 'submit']

driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

# CSS Selector, tagname[attribute = 'value'] -> input[@type = 'submit'], #ID, .classname

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Milica")
assert "success" in message

driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()

