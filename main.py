# Author: Julia Sabelli
# Date Created: 1/28/2024
# Description: Automated test script for the user login form of the OneBoss Demo website.
# Note: Test Case 4 is commented out to limit message spam on Indeed. Uncomment to run.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# This function automates the website login process using Selenium.
# It takes two parameters: `email` and `password`. It first opens a Chrome browser,
# navigates to the specified URL, and interacts with the webpage to perform a login operation.
# It waits for specific elements to be present and available before interacting with them.
# After the login operation, it waits for 2 seconds and then closes the browser.
def login_test(email, password):
    driver = webdriver.Chrome()
    url = "https://demo.oneboss.ca/repweb/client/login.xhtml"
    driver.get(url)

    # Wait for the email input field to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputEmail"))
    )
    driver.find_element(By.ID, "inputEmail").send_keys(email)

    # Wait for the password input field to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputPassword"))
    )
    driver.find_element(By.ID, "inputPassword").send_keys(password)

    # Wait for the login button to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btn"))
    )
    driver.find_element(By.ID, "btn").click()

    time.sleep(2)
    driver.quit()


# This function automates the website password reset process using Selenium.
# It takes four parameters: `user_type`, `email`, `last_3_sin`, and `dob`. It first opens a Chrome browser,
# navigates to the specified URL, and interacts with the webpage to perform a password reset operation.
# It waits for specific elements to be present and available before interacting with them.
# After the password reset operation, it waits for 2 seconds and then closes the browser.
def forgot_password_test(user_type, email, last_3_sin, dob):
    driver = webdriver.Chrome()
    url = "https://demo.oneboss.ca/repweb/client/login.xhtml"
    driver.get(url)

    dob = dob.split("-")

    dob_year = dob[0]
    dob_month = dob[1]
    dob_day = dob[2]

    # If dob_year is not 4 digits, print an error message.
    if len(dob_year) != 4 or ((int(dob_year) < 1900) or (int(dob_year) > 2010)):
        print("Invalid year.")

    # If dob_month is not in the dictionary, print an error message.
    dictionary = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May",
                  "06": "June", "07": "July", "08": "August", "09": "September", "10": "October",
                  "11": "November", "12": "December"}

    if dob_month in dictionary:
        dob_month = dictionary[dob_month]
    else:
        print("Invalid month.")

    # If dob_day is not 2 digits and equals 0, print an error message.
    if dob_day[0] == "0" and dob_day[1] != "0":
        dob_day = dob_day[1]
    elif dob_day[0] == "0" and dob_day[1] == "0":
        print("Invalid day.")

    # Wait for the Forgot Password button to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Forgot My Password']"))
    )
    driver.find_element(By.XPATH, "//input[@value='Forgot My Password']").click()

    # Use JavaScript to check the correct user type radio button.
    if user_type == 'individual':
        driver.execute_script("document.getElementById('forgotPasswordForm:j_idt14:0').checked = true;")
    elif user_type == 'corporation':
        driver.execute_script("document.getElementById('forgotPasswordForm:j_idt14:1').checked = true;")
    elif user_type == 'other':
        driver.execute_script("document.getElementById('forgotPasswordForm:j_idt14:2').checked = true;")

    # Wait for the email input field to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "forgotPasswordForm:j_idt17"))
    )
    driver.find_element(By.NAME, "forgotPasswordForm:j_idt17").send_keys(email)

    # Wait for the last 3 SIN input field to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "forgotPasswordForm:j_idt19"))
    )
    driver.find_element(By.NAME, "forgotPasswordForm:j_idt19").send_keys(last_3_sin)

    # Wait for the DOB year input field to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "forgotPasswordForm:j_idt22"))
    )
    driver.find_element(By.NAME, "forgotPasswordForm:j_idt22").send_keys(dob_year)

    # Wait for the DOB month input field to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "forgotPasswordForm:j_idt24"))
    )
    driver.find_element(By.NAME, "forgotPasswordForm:j_idt24").send_keys(dob_month)

    # Wait for the DOB day input field to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "forgotPasswordForm:j_idt26"))
    )
    driver.find_element(By.NAME, "forgotPasswordForm:j_idt26").send_keys(dob_day)

    # Wait for the confirm button to be present and interactive.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Confirm']"))
    )
    # Locate the confirm button again right before clicking it.
    confirm_button = driver.find_element(By.XPATH, "//input[@value='Confirm']")
    confirm_button.click()

    time.sleep(2)
    driver.quit()


# Test Case 1: Verify Login with Valid Credentials
# This test case uses valid credentials.
email_valid = "juliasabelliureg4_44g@indeedemail.com"
password_valid = "*Ferd_5424"
login_test(email_valid, password_valid)

# Test Case 2: Verify Login with Invalid Email
# This test case uses an invalid email.
email_invalid = "invalid_email@example.com"
password_invalid = "*Ferd_5424"
login_test(email_invalid, password_invalid)

# Test Case 3: Verify Login with Incorrect Password
# This test case uses an incorrect password.
email_valid_2 = "juliasabelliureg4_44g@indeedemail.com"
password_incorrect = "incorrect_password"
login_test(email_valid_2, password_incorrect)

# Test Case 4: Verify Forgot Password Link
# This test case clicks the Forgot Password link and uses valid credentials
# for an "individual" type user, to send a password reset email to the user's email address.
# user = "individual"
# email_valid_3 = "juliasabelliureg4_44g@indeedemail.com"
# last_3_sin_valid = "782"
# dob_valid = "2000-04-10"
# forgot_password_test(user, email_valid_3, last_3_sin_valid, dob_valid)
