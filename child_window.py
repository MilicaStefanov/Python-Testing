from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/shone/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

windows_open = driver.window_handles
driver.switch_to.window(windows_open[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(windows_open[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
