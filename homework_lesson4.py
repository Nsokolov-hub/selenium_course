from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://chat.deepseek.com/")

deepseek_titile = driver.title
print(deepseek_titile)

driver.get("https://stepik.org/learn")

stepik_title = driver.title
print(stepik_title)

driver.refresh()
url = driver.current_url

print(url)