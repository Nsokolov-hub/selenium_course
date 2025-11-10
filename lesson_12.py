from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument("--windows-size=1920, 1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Selenium")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5 , poll_frequency=1)

driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
time.sleep(10)
