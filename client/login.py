from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import traceback
import sys

def openLoginPage(driver):
    driver.get('https://hiringo.tech/auth/sign-in/')
    time.sleep(1)
    # check if title is correct
    assert 'Hiringo' in driver.title

def doLogin(email_addr, pwd, driver):
        driver.find_element(By.ID, 'email').send_keys(email_addr)

        driver.find_element(By.ID, 'password').send_keys(pwd)

        time.sleep(1)
        #/html/body/div/div[2]/div/form/div[3]/button
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[3]/button').click()

        time.sleep(3)
        # Check if dashboard page reached
        assert driver.find_element(By.CLASS_NAME, 'text-3xl').text == 'Dashboard'


# Login test
driver = webdriver.Firefox()
openLoginPage(driver)
try:
    doLogin('test@testing.test', 'test1234', driver)
except AssertionError:
    print("Assertion failed! Dashboard label not found")
except Exception:
    print(traceback.format_exc())
driver.close()