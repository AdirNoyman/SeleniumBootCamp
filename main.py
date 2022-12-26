from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/adirnoyman/Library/Mobile Documents/com~apple~CloudDocs/Documents/PythonCourses_ CodingEntrepreneurs/YouTubeCourses/PythonAutomation/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, chrome_options=options)

driver.get("https://www.harel-group.co.il/contact/Pages/customer-service.aspx")
driver.implicitly_wait(3)
my_element = driver.find_element(By.CSS_SELECTOR, 'button.CH-jss23')
my_element.click()