import subprocess
import sys

username = sys.argv[1]
status = sys.argv[2]

subprocess.Popen(["python3", "accept.py", username, status], shell=False)