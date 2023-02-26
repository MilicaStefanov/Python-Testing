from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/shone/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio_buttons[1].click()

assert radio_buttons[1].is_selected()
