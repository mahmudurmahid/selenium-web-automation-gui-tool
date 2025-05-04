from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
from dotenv import load_dotenv
load_dotenv()


class WebAutomation:
    def __init__(self):
        """
        Set required selenium options and service requirements, load webpage
        """        
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd() # Set the download path to the current working directory
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service("chromedriver-mac-x64/chromedriver")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)
        

    def login(self, username, password):
        """
        TASK A: AUTOMATE LOGIN
        """
        self.driver.get("https://demoqa.com/login") # Load the webpage

        # Find the username, password fields, and login button on webpage
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')
        
        # Fill in username and password details, and click the login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, full_name, email, current_address, permanent_address):
        """
        TASK B: AUTOMATE ELEMENTS > TEXT BOX FORM FILLING
        """
        # Locate the Elements Dropdown in Sidebar Menu and Text box option
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))) # Use XPATH when ID is not available
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Find the full name, email, current address, and permanent address fields; and submit button
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields with the required information, and submit the form
        full_name_field.send_keys(full_name)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download_file(self):
        """
        TASK C: AUTOMATE DOWNLOADING A FILE
        """
        # Locate the Elements Dropdown in Sidebar Menu and Download option
        upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download.click()
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close_browser(self):
        """
        Quit the browser after pressing Enter
        """
        input("Press Enter to close the browser")
        self.driver.quit()

if __name__ == "__main__":
    web_automation = WebAutomation()
    web_automation.login(os.getenv("LOGIN_USERNAME"), os.getenv("LOGIN_PASSWORD"))
    web_automation.fill_form(os.getenv("FULL_NAME"), os.getenv("EMAIL"), os.getenv("CURRENT_ADDRESS"), os.getenv("PERMANENT_ADDRESS"))
    web_automation.download_file()
    web_automation.close_browser()
