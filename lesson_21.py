from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)

driver.get("https://testkru.com/Elements/Buttons")

LEFT_BUTTON = ("xpath", "//button[@id='leftClick']")
DOUBLE_BUTTON = ("xpath", "//button[@id='doubleClick']")
CONTEXT_BUTTON = ("xpath", "//button[@id='rightClick']")

left_button_click = driver.find_element(*LEFT_BUTTON)
dooble_button_click = driver.find_element(*DOUBLE_BUTTON)
context_button_click = driver.find_element(*CONTEXT_BUTTON)
time.sleep(3)
action.click(left_button_click).perform()
time.sleep(3)

action.double_click(dooble_button_click).perform()
time.sleep(3)

action.context_click(context_button_click).perform()
time.sleep(3)