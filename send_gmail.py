# Author: Alex Luu
# Date: 20 April 2022
# Purpose: Logging in and sending an email through Selenium and Python
# In progress: Creating an email account, stalled by TFA


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r"PATH/TO/CHROMEDRIVER")
driver.implicitly_wait(10)

gmail = "https://www.google.com/gmail/about/"
driver.get(gmail)
driver.maximize_window()

# global variables
first_name = "FirstName"
last_name = "LastName"
# username = "automatedtest" + str(time.time())
username = "testingforalexautomation"
email = username + "@gmail.com"
password = "S0meP@ssword"

# info for sending email
to_email = email
subject = 'example subject'
body = 'example body'


# Clicks the "next" button for gmail, which is used multiple times

def gmail_next():
    next_button = wait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), \'Next\')]')))
    next_button.click()


# Creates a gmail account. Function is stalled at the moment due to TFA.

def create_gmail(create_first_name, create_last_name, create_username, create_password):
    get_gmail = driver.find_element(By.XPATH, "//span[contains(text(), 'Get Gmail')]")
    get_gmail.click()
    first_name_field = driver.find_element(By.ID, "firstName")
    first_name_field.send_keys(create_first_name)
    last_name_field = driver.find_element(By.ID, "lastName")
    last_name_field.send_keys(create_last_name)
    username_field = last_name_field = driver.find_element(By.ID, "username")
    username_field.send_keys(create_username)
    password_field = driver.find_element(By.NAME, "Passwd")
    password_field.send_keys(create_password)
    confirm_password_field = driver.find_element(By.NAME, "ConfirmPasswd")
    confirm_password_field.send_keys(create_password)
    gmail_next()
    # next steps involve a phone, so this is going to be manual for now
    # therefore this function is incomplete


# Logging into gmail with an existing account that's been used on this computer before

def log_into_gmail(login_email, login_password):
    driver.get('https://www.google.com/gmail/about/')
    sign_in_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
    sign_in_button.click()
    input_email = driver.find_element(By.ID, "identifierId")
    input_email.send_keys(login_email)
    gmail_next()
    input_password = driver.find_element(By.CSS_SELECTOR, "[aria-label*='Enter your password']")
    input_password.send_keys(login_password)
    gmail_next()


# send an email with basic text

def send_email(target_email, email_subject, body_content):
    compose_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Compose')]")
    compose_button.click()
    to_field_enter = driver.find_element(By.NAME, "to")
    to_field_enter.send_keys(target_email)
    subject_title = driver.find_element(By.NAME, "subjectbox")
    subject_title.send_keys(email_subject)
    email_body = driver.find_element(By.CSS_SELECTOR, "[role*='textbox']")
    email_body.send_keys(body_content)
    send_button = wait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@aria-label, '(Ctrl-Enter)')]")))
    send_button.click()


def test():
    # create_gmail(first_name, last_name, username, password)
    log_into_gmail(email, password)
    send_email(to_email, subject, body)
