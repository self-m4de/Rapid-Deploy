import json
import requests
import connect

api_token = connect.connect()
api_url_base = 'https://api.digitalocean.com/v2/'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


def create_new_droplet(name):

    api_url = '{0}droplets'.format(api_url_base)

    new_droplet = {'name': name, 'region': 'sfo2', 'size': 's-1vcpu-1gb', 'image': '49211392'}

    response = requests.post(api_url, headers=headers, json=new_droplet)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(new_droplet)
        print(response.content)
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 202:
        print("Your new droplet was created:")
        print(name)
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None

