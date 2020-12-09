"""
a simple website blocker worked by redirecting desired website's ip
to ip "127.0.0.1" which is the localhost
"""

import time
from datetime import datetime, timedelta
import platform
import os



def blocker(values, block_time):

    block_list_path = os.getcwd()

    Linux = "/etc/hosts"
    Windows = r"C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"
    host_path = ""

    if platform.system() == "Linux" or platform.system() == "Darwin":
        host_path = Linux
        block_list_path  = block_list_path+"/block_list.txt"
    elif platform.system() == "Windows":
        host_path = Windows
        block_list_path = block_list_path+r"\block_list.txt"

    sites_to_block = []
    if values[1]:
        social_media = []
        with open(block_list_path, "r") as lists:
            list = lists.readlines()
            sm_index = list.index("social_media:\n")
            for i in range(sm_index, len(list)):
                if list[i] == "\n":
                    break
                list[i] = list[i][:list[i].rfind("\n")]
                if list[i] != "social_media:":
                    social_media.append("www."+list[i]+".com")
                    social_media.append(list[i]+".com")

        sites_to_block.extend(social_media)
    if values[2]:
        entertainment = []
        with open(block_list_path, "r") as lists:
            list = lists.readlines()
            ent_index = list.index("entertainment:\n")
            for i in range(ent_index, len(list)):
                if list[i] == "\n":
                    break
                list[i] = list[i][:list[i].rfind("\n")]
                if list[i] != "entertainment:":
                    entertainment.append("www." + list[i] + ".com")
                    entertainment.append(list[i] + ".com")
        sites_to_block.extend(entertainment)
    if values[3]:
        shopping = []
        with open(block_list_path, "r") as lists:
            list = lists.readlines()
            shop_index = list.index("shopping:\n")
            for i in range(shop_index, len(list)):
                if list[i] == "\n":
                    break
                list[i] = list[i][:list[i].rfind("\n")]
                if list[i] != "shopping:":
                    shopping.append("www." + list[i] + ".com")
                    shopping.append(list[i] + ".com")
        sites_to_block.extend(shopping)


    for i in range(4,9):
        if values[i] is not None:
            values[i].split(.)
            sites_to_block.append("www." + values[i] + ".com")
            sites_to_block.append(values[i]+".com")

    for i in range(9, 14):
        if values[i] is not None:
            if "www." + values[i] + ".com" in sites_to_block:
                sites_to_block.remove("www." + values[i] + ".com")
                sites_to_block.remove(values[i] + ".com")


    current_time = datetime.now()
    block_time_sec = block_time * 60
    blocker_end_time = current_time + timedelta(0, block_time_sec)
    print(blocker_end_time)
    blocker_status = True

    while blocker_status:
        if datetime.now() < blocker_end_time:
            with open(host_path, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                        hostfile.write(redirect + ' ' + site + '\n')
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


