import requests
from urllib import parse


def login(username, password):
    login_data = {'username': username, 'password': password}
    print(login_data)
    r = requests.post('http://127.0.0.1:8000/api-token-auth/', data=login_data)
    print(r.text)
    if r.status_code == 200:
        response = r.json()
        return response['token']
    return None

def get_blocked_sites(token):
    headers = {'Authorization': 'Token ' + token}
    r = requests.get('http://127.0.0.1:8000/api/block/', headers=headers)

    if r.status_code == 200:
        response = r.json()
        blocked_sites = []
        for record in response:
            blocked_sites.append(parse.urlparse(record['site_url']).netloc)
        return blocked_sites
    return None

def send_blocked_sites(token, blocked_sites):
    headers = {'Authorization': 'Token ' + token}
    old_block_list = set(get_blocked_sites(token))
    new_block_list = set(blocked_sites) - old_block_list

    data = [{'site_url': 'https://' + site} for site in new_block_list]
  #  r = requests.post('http://127.0.0.1:8000/api/block/', headers=headers, data=data)

    for d in data:
        r = requests.post('http://127.0.0.1:8000/api/block/', headers=headers, data=d)
        if r.status_code == 200:
            return 0
        return -1
