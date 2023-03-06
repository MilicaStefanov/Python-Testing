import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/shone/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("contact@rahulshettyacademy.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('learning')
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

windows_open = driver.window_handles
driver.switch_to.window(windows_open[1])

mail = driver.find_element(By.CSS_SELECTOR, "div p:nth-child(2) a").text

windows_open = driver.window_handles
driver.switch_to.window(windows_open[0])

driver.find_element(By.XPATH, "//input[@id='username']").clear()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(mail)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

time.sleep(2)
message = driver.find_element(By.CSS_SELECTOR, '.alert.alert-danger.col-md-12').text
print(message)

