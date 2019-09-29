import time
import os
import sys


username = sys.argv[1]


os.chdir(f'./profiles/{username}')

otp_filename = username + "_result.txt"
file_list = os.listdir()

while otp_filename not in file_list:
    time.sleep(1)
    file_list = os.listdir()


otp_file = open(otp_filename, "r")
otp = otp_file.read()
otp_file.close()
print(otp)