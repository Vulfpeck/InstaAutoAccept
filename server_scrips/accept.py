import time 
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


accepted_count = 0

def acceptRequests(accept_limit):
    global accepted_count

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.headless = True
    options.add_argument(f'user-data-dir=./profile')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path = "/home/abhishek_nexus26/chromedriver", options = options)
    print (driver.desired_capabilities)
    driver.get('https://www.instagram.com/accounts/activity/?followRequests=1')
    time.sleep(10)
    confirm_request_button_list = driver.find_elements_by_xpath("//*[contains(text(), 'Confirm')]")
    print(confirm_request_button_list)
    print(driver.title)
    for confirm_button in confirm_request_button_list:
        try: 
            confirm_button.click()
            accepted_count += 1
            accept_limit -= 1
        except:
            print("button no found")
            break

        if accept_limit <= 0:
            time.sleep(2)
            driver.close()
            break
    time.sleep(2)
    driver.close()

if __name__ == "__main__":
    
    username = sys.argv[1]
    mode = sys.argv[2]

    os.chdir(f"./profiles/{username}/")
    hourly_accept_limit = 9500
    status_filename = username + "_status.txt"
    try: 
        count_file = open(f"./{username}_count.txt", "r")
        curr_count = count_file.read()
        print(curr_count)
        if curr_count== '':
            accepted_count = 0
        else:
            accepted_count = int(curr_count)
        
        print("Input from file" + count_file.readline())
        print("parse: " + str(accepted_count))
        count_file.close()
    except:
        print("failed to read file, assuming new user")
        accepted_count = 0
        pass
    # count_file = open(f"./{username}_count.txt", "w")
    # count_file.write("str(accepted_count)")
    # count_file.close()
    while True:
        
        with open(f"./{status_filename}", "r") as status_file:
            status = status_file.read().split('\n')[0]
            print(status)
        if status == "on":
            print("status turned on")
            acceptRequests(hourly_accept_limit)
            print("Accepted count:" + str(accepted_count))
            with open(f"./{username}_count.txt", "w") as count_file:
                count_file.write(str(accepted_count))
            time.sleep(10)
        else:
            quit()
