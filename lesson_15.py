from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Добавлен импорт
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox_1 = (By.XPATH, "//input[1]")  # Исправлено
time.sleep(3)
driver.find_element(*checkbox_1).click()
time.sleep(3)