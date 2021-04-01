import datetime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#
current_month = str.lower(datetime.datetime.now().strftime("%B"))
current_year = str.lower(datetime.datetime.now().strftime("%Y"))
link = f"https://rebrainme.com/webinars/devops-{current_month}-{current_year}/"

user_name = "username"
user_email = "example@example.edu"
user_phone_number = "+79991235678"

print(link)

browser = webdriver.Chrome()
browser.get(link)

BUTTON_REGISTER = (By.CSS_SELECTOR, ".btn-bottom-register")
button_register = browser.find_element(*BUTTON_REGISTER)
browser.execute_script("return arguments[0].scrollIntoView(true);", button_register)
button_register.click()


USER_NAME_FIELD = (By.CSS_SELECTOR, ".userName")
USER_EMAIL_FIELD = (By.CSS_SELECTOR, ".userEmail")
USER_PHONE_FIELD = (By.CSS_SELECTOR, ".userPhone")
BUTTON_REGISTER_FORM = (By.CSS_SELECTOR, ".inputform .btn-register")

browser.find_element(*USER_NAME_FIELD).send_keys(user_name)
browser.find_element(*USER_EMAIL_FIELD).send_keys(user_email)
browser.find_element(*USER_PHONE_FIELD).send_keys(user_phone_number)
# browser.find_element(*BUTTON_REGISTER_FORM).click()

time.sleep(5)
browser.close()
