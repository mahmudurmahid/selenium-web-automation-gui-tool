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

# Find the username, password fields, and login button on webpage
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

# Fill in username and password details, and click the login button
username_field.send_keys(os.getenv("LOGIN_USERNAME"))
password_field.send_keys(os.getenv("LOGIN_PASSWORD"))
login_button.click()




# Quit the browser after pressing Enter
input("Press Enter to close the browser")
driver.quit()
