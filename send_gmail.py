# Author: Alex Luu
# Date: 20 April 2022
# Last Updated: 26 April 2022
# Purpose: Logging in and sending an email through Selenium and Python
# In progress: Classes and function overloading


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
list_of_fonts = ['Sans Serif', 'Serif', 'Fixed Width', 'Wide', 'Narrow', 'Comic Sans MS',
                 'Garamond', 'Georgia', 'Tahoma', 'Trebuchet MS', 'Verdana']


# Clicks the "next" button for gmail, which is used multiple times

def gmail_next():
    next_button = wait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), \'Next\')]')))
    next_button.click()


# Logging into gmail with an existing account that's been used on this computer before

def log_into_gmail(login_email, login_password):
    try:
        driver.get('https://www.google.com/gmail/about/')
        sign_in_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
        sign_in_button.click()
        input_email = driver.find_element(By.ID, "identifierId")
        input_email.send_keys(login_email)
        gmail_next()
        input_password = driver.find_element(By.CSS_SELECTOR, "[aria-label*='Enter your password']")
        input_password.send_keys(login_password)
        gmail_next()
    except Exception:
        # sometimes it needs to retry
        log_into_gmail(login_email, login_password)


# Change font

def change_font(font_number_from_list):
    try:
        formatting_button = wait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@data-tooltip, 'Formatting options')]")))
        formatting_button.click()
        default_font = wait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@aria-label, '(Ctrl-Shift-5, Ctrl-Shift-6)')]")))
        default_font.click()
        new_font = wait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '" +
                                        list_of_fonts[font_number_from_list] + "')]")))
        new_font.click()
    except Exception:
        # sometimes needs to be done twice
        change_font(font_number_from_list)


# send an email with choice in font

def send_email_new_font(target_email, email_subject, body_content, font_number):
    compose_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Compose')]")
    compose_button.click()
    to_field_enter = wait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "to")))
    to_field_enter.send_keys(target_email)
    subject_title = wait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "subjectbox")))
    subject_title.send_keys(email_subject)
    change_font(font_number)
    email_body = wait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[role*='textbox']")))
    email_body.send_keys(body_content)
    send_button = wait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@aria-label, '(Ctrl-Enter)')]")))
    send_button.click()


#  for default font only

def send_email(target_email, email_subject, body_content):
    compose_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Compose')]")
    compose_button.click()
    to_field_enter = wait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "to")))
    to_field_enter.send_keys(target_email)
    subject_title = wait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "subjectbox")))
    subject_title.send_keys(email_subject)
    email_body = wait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[role*='textbox']")))
    email_body.send_keys(body_content)
    send_button = wait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@aria-label, '(Ctrl-Enter)')]")))
    send_button.click()


def test():
    log_into_gmail(email, password)
    send_email_new_font(to_email, subject, body, 2)
    driver.close()
