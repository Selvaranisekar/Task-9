import selenium

from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(5)

username_input = driver.find_element("id","user-name")
password_input = driver.find_element("id","password")
login_button = driver.find_element("xpath","//input[@type='submit']")

# Input data
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")

# Click the login button
login_button.click()
time.sleep(5)

#URL of the Web page

Current_URL = driver.current_url
print("Current URL of the Web Page is: ", Current_URL)

#Tile of the Web page

Title = driver.title
print("Title of the web page is :", Title)

page_source=driver.page_source
print(page_source)

# open result.html
# file = open("C:/Users/ssekar588/PycharmProjects/GUVI_Selenium/Webpage_task_11.txt",'w')
file = open("Webpage_task_11.txt",'w')

# Write the entire page content in result.html
file.write(page_source)
file.close()




