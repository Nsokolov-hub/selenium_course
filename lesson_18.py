from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/login")
time.sleep(5)
print(driver.window_handles)
# Клик по кнопке, которая открывает новую вкладку
FOR_BUSINESS_BUTTON = ("xpath", "//a[text()=' For Business ']")
driver.find_element(*FOR_BUSINESS_BUTTON).click()
time.sleep(3)

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

START_FOR_FREE_BUTTON = ("xpath", "(//a[text()='Start for Free'])[1]")
driver.find_element.click(*START_FOR_FREE_BUTTON).click()
time.sleep(3)