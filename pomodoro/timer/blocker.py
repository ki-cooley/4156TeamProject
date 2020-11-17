import time
from datetime import datetime, timedelta

# sample websites that will be blocked
sites_to_block = [
    "www.facebook.com",  "facebook.com",
    "www.youtube.com", "youtube.com",
    "www.gmail.com", "gmail.com"
]

Linux = "/etc/hosts"
Windows = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
host_path = ""
set_os = False

while not set_os:
    oper_sys = input("Please indicate your operating system (Linux/Windows): ")

    if oper_sys == "Linux":
        host_path = Linux
        set_os = True
    elif oper_sys == "Windows":
        host_path = Windows
        set_os = True
    else:
        print("Please enter a valid operating system")

block_time = 0
while block_time <= 0:
    block_time = int(input("Please enter number of minutes you would like the blocker to work: "))

current_time = datetime.now()
block_time_sec = block_time*60
blocker_end_time = current_time + timedelta(0,block_time_sec)
print(blocker_end_time)
blocker_status = True

while blocker_status:
    if datetime.now() < blocker_end_time:
        with open(host_path, 'r+') as hostfile:
            hosts = hostfile.read()
            for site in  sites_to_block:
                if site not in hosts:
                   hostfile.write(redirect+' '+site+'\n')
        print("website blocker is activated ... ")
        time.sleep(5)
    else:
        with open(host_path, 'r+') as hostfile:
            hosts = hostfile.readlines()
            hostfile.seek(0)
            for host in hosts:
                if not any(site in host for site in sites_to_block):
                    hostfile.write(host)
            hostfile.truncate()
        print('Blocking time is over. Good job!')
        blocker_status = False

