from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/")
time.sleep(3)

login_button = driver.find_element("xpath", "//button[@type='submit']")
login_button.click()

time.sleep(3)


email_field = driver.find_element("xpath", "//input[@id='formBasicEmail']")
email_field.send_keys("test-eamail@mail.com")
time.sleep(3)
print(email_field.get_attribute("value"))
time.sleep(3)
email_field.clear()
time.sleep(3)