from selenium import webdriver

from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/Users/shone/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# using Selenium for JavaScript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
