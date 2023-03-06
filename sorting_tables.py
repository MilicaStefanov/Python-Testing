from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browser_sorted_veggies = []
service_obj = Service("/Users/shone/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")


driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggie_web_elements = driver.find_elements(By.XPATH, "//tr/td[1]")

for element in veggie_web_elements:
    browser_sorted_veggies.append(element.text)

original_browser_sorted_list = browser_sorted_veggies.copy()
browser_sorted_veggies.sort()

assert browser_sorted_veggies == original_browser_sorted_list
