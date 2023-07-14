from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from faker.providers import BaseProvider

import names
import string
import secrets
import time

fake = Faker()

# Path to your ChromeDriver executable
# chrome_driver_path = 'C:\webdrivers/chromedriver.exe'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome()

# URL to open
url = 'https://sumoquoteweb-qa.azurewebsites.net/new-account'

# Open the URL in the Chrome browser
driver.get(url)

# Close the browser window
# driver.quit()

# Wait for the Organization Name field to be visible
wait = WebDriverWait(driver, 10)
org_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="accountName"]')))
first_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="firstName"]')))
last_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="lastName"]')))
email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="emailAddress"]')))
phone_number = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="phoneNumber"]')))
password_loc = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="Password"]')))
repeat_password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="repeatPassword"]')))
how_heard = driver.find_element(By.CSS_SELECTOR, '[class="v-input__icon v-input__icon--append"]')
# clickable = driver.get('[class="v-input__icon v-input__icon--append"]')

fake_first_name = names.get_first_name()
fake_last_name = names.get_last_name()
fake_email = fake.email()
fake_phone = fake.msisdn()
fake_company = fake.company()
password=fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
#print(password)

driver.maximize_window()
# Fill the Organization Name field
org_name_input.send_keys(fake_company)
first_name.send_keys(fake_first_name)
last_name.send_keys(fake_last_name)
email.send_keys(fake_email)
phone_number.send_keys(fake_phone)
password_loc.send_keys(password)
repeat_password.send_keys(password)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", how_heard)
driver.find_element(By.CSS_SELECTOR, '[class="v-input__icon v-input__icon--append"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[id="list-item-477-5"]').click()
# time.sleep(2)
#Select I agree to the terms and condition check
driver.find_element(By.CSS_SELECTOR, '[class="v-input--selection-controls__ripple"]').click()
# Make sure the Save button is enabled
save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn-sumo-primary v-btn v-btn--has-bg '
                                                                      'theme--light elevation-0 v-size--default"]')))
save_button.click()


driver.quit()
