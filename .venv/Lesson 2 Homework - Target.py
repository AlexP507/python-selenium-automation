from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#unit driver
driver = webdriver.Chrome()
driver.maximize_window()

#open the url
driver.get("https://www.target.com/")

sleep(5)

#Click Account button
account_button = driver.find_element(By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3' and text()='Account']")
account_button.click()

sleep(5)

#Click SignIn btn from side navigation
signin_button = driver.find_element(By.XPATH,   "//button[text()='Sign in or create account']")
signin_button.click()

sleep(5)

#Verify SignIn page opened:
#1) “Sign in or create account” text is shown,
#THIS WORKS IF THE PREVIOUS STEP OF CLICKING THE SIGN IN BUTTON IS OMITTED, OTHERWISE THE COMMAND IS OUT OF ORDER OF HOW TARGET WEBSITE IS DESIGNED
expected_text = "Sign in or create account"
text_element = driver.find_element(By.XPATH, ("//button[@data-test='accountNav-signIn' and text()='Sign in or create account']"))
actual_text =text_element.text

assert expected_text in actual_text
print('Test case passed')

#2) SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here) =
signin_shown = driver.find_element(By.XPATH,    "//button[@type='button' and @data-test='accountNav-signIn']")

