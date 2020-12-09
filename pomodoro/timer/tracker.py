import browserhistory as bh
from urllib import parse
from requests import post
import json

def track(token):
    history = bh.get_browserhistory()['chrome']
    #needs to be changed to provide real authentication
    session_activity = [{'site_url': strip_url(x[0]), 'visit_timestamp': x[2], 'user_id': user_id} for x in history]
    activity_json = json.dumps(session_activity)
    headers = {'Authorization': 'Token ' + token}
    r = post('http://127.0.0.1:8000/api/track/', json=session_activity, headers=headers)

def strip_url(url):
    stripped_url = parse.urlparse(url).scheme + "://" + parse.urlparse(url).netloc
    return stripped_url
