from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

###########################################################

#enter the link to the website you want to automate login.
website_link=""
#enter your login username
username=""
#enter your login password
password=""

###########################################################

#enter the element for username input field
element_for_username=""
#enter the element for password input field
element_for_password=""
#enter the element for submit button
element_for_submit=""

###########################################################



browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]
browser.get((website_link))	

try:
	username = browser.find_element_by_name(element_for_username)
	username.send_keys(username)		
	password  = browser.find_element_by_name(element_for_password)
	password.send_keys(password)
	signInButton = browser.find_element_by_name(element_for_submit)
	signInButton.click()
	time.sleep(3)
	browser.quit()
	time.sleep(1)
	browserExe = "Safari"
	os.system("pkill "+browserExe)
except Exception:
	browser.quit()
	browserExe = "Safari"
	os.system("pkill "+browserExe)


