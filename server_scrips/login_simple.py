import time 
import sys
import os
import subprocess

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import shutil

username = sys.argv[1]
passwd = sys.argv[2]

# For security reasons, this script will remove the directory of the user every time he logs in
if username in os.listdir('./profiles'):
    shutil.rmtree(f'./profiles/{username}')

# and then create it again
os.mkdir(f'./profiles/{username}')
os.chdir(f'./profiles/{username}/')
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.headless = True
options.add_argument(f'user-data-dir=./profile')
driver = webdriver.Chrome(executable_path = "/home/abhishek_nexus26/chromedriver", options = options)
actions = ActionChains(driver)
print(driver.desired_capabilities)
login_url = "https://www.instagram.com/accounts/login/"
driver.get(login_url)
time.sleep(2)
uname_field = driver.find_element_by_name("username")
pwd_field = driver.find_element_by_name("password")

# this will return a list of web elements instead of a web element, as we search with regex
submit_button = driver.find_elements_by_xpath("//*[contains(text(), 'Log In')]")

uname_field.send_keys(username)
pwd_field.send_keys(passwd)

time.sleep(1)
submit_button[0].click()
time.sleep(3)
if driver.current_url == login_url:
   print("error")
   driver.close()
   quit() 


time.sleep(25)
# check redirect url to see what flow to follow
print('login done')

driver.close()
