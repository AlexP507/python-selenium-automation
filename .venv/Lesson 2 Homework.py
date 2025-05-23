from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#unit driver
driver = webdriver.Chrome()
driver.maximize_window()

#open the url
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

sleep (8)

#LOCATORS
#amazon logo - XPATH
driver.find_element(By.XPATH,   "//i[@class='a-icon a-icon-logo' and @role='presentation']")

#email field - ID
driver.find_element(By.ID,  'ap_email')

#continue button - ID
driver.find_element(By.ID,  'continue')

#Conditions of use link - XPATH
driver.find_element(By.XPATH,   "//a[text()='Conditions of Use']")

#Privacy notice link - XPATH
driver.find_element(By.XPATH,   "//a[text()='Privacy Notice']")

#Need help link - XPATH
driver.find_element(By.XPATH,   "//span[@class='a-expander-prompt']")

#forgot your password link - ID
driver.find_element(By.ID,  'auth-fpp-link-bottom')

#other issues with sign-in link - ID
driver.find_element(By.ID,  'ap-other-signin-issues-link')

#create your amazon account button - ID
driver.find_element(By.ID,  'createAccountSubmit')