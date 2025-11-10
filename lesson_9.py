from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--incognito")
# options.add_argument("--window-size=700,700")
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1920, 1080)

driver.get("https://aliexpress.ru/")
time.sleep(3)