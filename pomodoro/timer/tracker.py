import browserhistory as bh
from urllib import parse
from requests import post
import json
def main():
    history = bh.get_browserhistory()['chrome']
    #needs to be changed to provide real authentication
    user_id = input("Insert your user id: ")
    session_activity = [{'site_url': strip_url(x[0]), 'visit_timestamp': x[2], 'user_id': user_id} for x in history]
    activity_json = json.dumps(session_activity)

    r = post('http://127.0.0.1:8000/api', json=activity_json)

def strip_url(url):
    stripped_url = parse.urlparse(url).netloc
    return stripped_url

if __name__ == "__main__":
    main()