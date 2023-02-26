from selenium import webdriver

from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/shone/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.facebook.com/MilicaaStefanoov/")

print(driver.title)
print(driver.current_url)

#driver.get("https://rahulshettyacademy.com/practice-project")
driver.minimize_window()

#driver.back()
driver.refresh()
#driver.forward()

driver.close()
