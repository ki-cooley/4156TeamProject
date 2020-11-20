"""
a simple website blocker worked by redirecting desired website's ip
to ip "127.0.0.1" which is the localhost
"""

import time
from datetime import datetime, timedelta

# sample websites that will be blocked
sites_to_block = [
    "www.facebook.com",  "facebook.com",
    "www.youtube.com", "youtube.com",
    "www.gmail.com", "gmail.com"
]

# host path specific to os
LINUX = "/etc/hosts"
WINDOWS = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT = "127.0.0.1"
HOST_PATH = ""
SET_OS = False

# asking for user input of os, will change to obtain from the website
while not SET_OS:
    oper_sys = input("Please indicate your operating system (Linux/Windows): ")

    if oper_sys == "Linux":
        HOST_PATH = LINUX
        SET_OS = True
    elif oper_sys == "Windows":
        HOST_PATH = WINDOWS
        SET_OS = True
    else:
        print("Please enter a valid operating system")

# asking for user input of block time, will change to obtain from the website
BLOCK_TIME = 0
while BLOCK_TIME <= 0:
    block_time = int(input("Please enter number of minutes you would like the blocker to work: "))

current_time = datetime.now()
BLOCK_TIME_SEC = BLOCK_TIME*60
blocker_end_time = current_time + timedelta(0,BLOCK_TIME_SEC)
print(blocker_end_time)
BLOCKER_STATUS = True

# blocking functionality
while BLOCKER_STATUS:
    if datetime.now() < blocker_end_time:
        with open(HOST_PATH, 'r+') as hostfile:
            hosts = hostfile.read()
            for site in  sites_to_block:
                if site not in hosts:
                    hostfile.write(REDIRECT+' '+site+'\n')
        print("website blocker is activated ... ")
        time.sleep(5)
    else:
        with open(HOST_PATH, 'r+') as hostfile:
            hosts = hostfile.readlines()
            hostfile.seek(0)
            for host in hosts:
                if not any(site in host for site in sites_to_block):
                    hostfile.write(host)
            hostfile.truncate()
        print('Blocking time is over. Good job!')
        BLOCKER_STATUS = False
