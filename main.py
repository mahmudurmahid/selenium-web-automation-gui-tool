from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
from dotenv import load_dotenv
load_dotenv()
# Set required selenium options and service requirements, load webpage
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service("chromedriver-mac-x64/chromedriver")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("https://demoqa.com/login") # Load the webpage

"""
TASK A: AUTOMATE LOGIN
"""
# Find the username, password fields, and login button on webpage
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in username and password details, and click the login button
username_field.send_keys(os.getenv("LOGIN_USERNAME"))
password_field.send_keys(os.getenv("LOGIN_PASSWORD"))
driver.execute_script("arguments[0].click();", login_button)

"""
TASK B: AUTOMATE ELEMENTS > TEXT BOX FORM FILLING
"""
# Locate the Elements Dropdown in Sidebar Menu and Text box option
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))) # Use XPATH when ID is not available
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Find the full name, email, current address, and permanent address fields; and submit button
full_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Fill in the form fields with the required information, and submit the form
full_name_field.send_keys(os.getenv("FULL_NAME"))
email_field.send_keys(os.getenv("EMAIL"))
current_address_field.send_keys(os.getenv("CURRENT_ADDRESS"))
permanent_address_field.send_keys(os.getenv("PERMANENT_ADDRESS"))
driver.execute_script("arguments[0].click();", submit_button)

# Quit the browser after pressing Enter
input("Press Enter to close the browser")
driver.quit()
