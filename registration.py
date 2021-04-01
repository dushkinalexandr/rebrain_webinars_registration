import datetime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

current_month = str.lower(datetime.datetime.now().strftime("%B"))
current_year = str.lower(datetime.datetime.now().strftime("%Y"))
link = f"https://rebrainme.com/webinars/devops-{current_month}-{current_year}/"

user_name = "Xander"
user_email = "123@gmail.com"
user_phone_number = "+79991235678"

print(link)

browser = webdriver.Chrome()
browser.get(link)

BUTTON_REGISTER = (By.CSS_SELECTOR, ".btn-bottom-register")
button_register = browser.find_element(*BUTTON_REGISTER)
browser.execute_script("return arguments[0].scrollIntoView(true);", button_register)
button_register.click()

time.sleep(3)
browser.close()
