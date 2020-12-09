"""
a simple website blocker worked by redirecting desired website's ip
to ip "127.0.0.1" which is the localhost
"""

import time
from datetime import datetime, timedelta
import platform
import os
from django.contrib.auth.models import User
from . import models as m

def blocker(values, block_time, id):

    """
    blocker function that takes blocking info from user (blocker gui) and writes it to the
    hosts file. It also sends a list of blocked sites to the database
    :param values: dictionary obtained from blocker gui containing blocking info
    :param block_time: how long the blocker works, obtained from blocker gui
    :return: no return value
    """

    block_list_path = os.getcwd()
    clean_block_list = []

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
    # category 1
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
    # category 2
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
    # category 3
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

    # personalized block list
    for i in range(4,9):
        if values[i] is not None:
            val = values[i].split(".")
            if len(val) == 1 and values[i]+".com" not in sites_to_block:
                sites_to_block.append("www." + values[i] + ".com")
                sites_to_block.append(values[i]+".com")
            if len(val) == 2:
                if val[0] == "www" and val[1] != "com" and values[i]+".com" not in sites_to_block:
                    sites_to_block.append(values[i] + ".com")
                    sites_to_block.append(val[1]+".com")
                if val[1] == "com" and val[0] != "www" and "www."+values[i] not in sites_to_block:
                    sites_to_block.append("www."+values[i])
                    sites_to_block.append(values[i])
            if len(val) == 3:
                if val[0] == "www" and val[2] == "com" and values[i] not in sites_to_block:
                    sites_to_block.append(values[i])
                    sites_to_block.append(val[1]+"."+val[2])

    # white list
    for i in range(9, 14):
        if values[i] is not None:
            val = values[i].split(".")
            if len(val) == 1:
                if "www." + values[i] + ".com" in sites_to_block:
                    sites_to_block.remove("www." + values[i] + ".com")
                    sites_to_block.remove(values[i] + ".com")
            if len(val) == 2:
                if val[0] == "www" and val[1]+".com" in sites_to_block:
                    sites_to_block.remove(values[i]+".com")
                    sites_to_block.remove(val[1] + ".com")
                if val[1] == "com" and values[i] in sites_to_block:
                    sites_to_block.remove(values[i])
                    sites_to_block.remove("www."+values[i])
            if len(val) == 3:
                if val[0] == "www" and val[2] == "com" and values[i] in sites_to_block:
                    sites_to_block.remove(values[i])
                    sites_to_block.remove(val[1] + "." + val[2])

    insert_to_bd(id, sites_to_block)

    current_time = datetime.now()
    block_time_sec = block_time * 60
    blocker_end_time = current_time + timedelta(0, block_time_sec)
    blocker_status = True

    while blocker_status:
        if datetime.now() < blocker_end_time:
            with open(host_path, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                        hostfile.write(redirect + ' ' + site + '\n')
            print("website blocker is activated ... ")
            time.sleep(300)
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


def insert_to_bd(user, sites_to_block):
    """

    :param user: user id
    :param sites_to_block: passed in from blocker()
    :return: no return value
    """

    sites = m.BlockedSite()
    sites.user_id = user
    sites.site_url = sites_to_block
    sites.save()


