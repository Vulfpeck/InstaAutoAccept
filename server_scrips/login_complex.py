import time
import sys
import os

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
options.headless = True
options.add_argument(f'user-data-dir=./profile')
driver = webdriver.Chrome(executable_path = "/home/abhishek_nexus26/chromedriver", options = options)
actions = ActionChains(driver)

login_url = "https://www.instagram.com/accounts/login/"

driver.get(login_url)
time.sleep(2)

uname_field = driver.find_element_by_name("username")
pwd_field = driver.find_element_by_name("password")

# this will return a list of web elements instead of a web element, as we search with regex
submit_button = driver.find_elements_by_xpath(
    "//*[contains(text(), 'Log In')]")

uname_field.send_keys(username)
pwd_field.send_keys(passwd)

time.sleep(1)
submit_button[0].click()

time.sleep(2)

if driver.current_url != "https://www.instagram.com/accounts/login/two_factor":
    print("error")
    driver.close()
    quit()


otp_filename = username + "_otp.txt"
file_list = os.listdir()

# Wait for the file to be created
while otp_filename not in file_list:
    time.sleep(1)
    file_list = os.listdir()

time.sleep(2)
otp_file = open(otp_filename, "r")
otp = otp_file.readline().split("\n")[0]
print(otp)

otp_file.close()

verification_code_field = driver.find_element_by_name("verificationCode")
verification_code_field.click()
submit_otp_button = driver.find_elements_by_xpath(
    "//*[contains(text(), 'Confirm')]")


#driver.execute_script(f"document.getElementsByName('verificationCode')[0].setAttribute('value', {otp})")
for x in otp:
        verification_code_field.send_keys(x)
        time.sleep(0.1)

time.sleep(1)
submit_otp_button[0].click()

time.sleep(30)

if driver.current_url == "https://www.instagram.com/accounts/login/two_factor":
    print("error")
else:
    print("done")

driver.close()
