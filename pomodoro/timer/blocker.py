import time
from datetime import datetime, timedelta
import platform

def blocker(values, block_time):

    # sample websites that will be blocked
    social_media = [
        "www.facebook.com", "facebook.com",
        "www.twitter.com", "twitter.com",
        "www.whatsapp.com", "whatsapp.com",
        "www.tumblr.com", "tumblr.com",
        "www.reddit.com", "reddit.com"
        "www.pinterest.com", "pinterest.com",
        "www.sina.com", "sina.com"
    ]

    entertainment = [
        "www.youtube.com", "youtube.com",
        "www.tiktok.com", "tiktok.com",
        "www.hulu.com", "hulu.com"
        "www.steam.com", "steam.com",
        "www.crunchyroll.com", "crunchyroll.com",
        "www.douban.com", "douban.com"

    ]

    shopping = [
        "www.amazon.com", "amazon.com",
        "www.sephora.com", "sephora.com",
        "www.asos.com", "asos.com",
        "www.bestbuy.com", "bestbuy.com",
        "www.macys.com", "macys.com",
        "www.ebay.com", "ebay.com",
        "www.zappos.com", "zappos.com"
        "www.costco.com", "costco.com",
        "www.bjs.com", "bjs.com"
    ]

    sites_to_block = []
    if values[1]:
        sites_to_block.extend(social_media)
    if values[2]:
        sites_to_block.extend(entertainment)
    if values[3]:
        sites_to_block.extend(shopping)


    Linux = "/etc/hosts"
    Windows = r"C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"
    host_path = ""

    if platform.system() == "Linux" or platform.system() == "Darwin":
        host_path = Linux
    elif platform.system() == "Windows":
        host_path = Windows

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
