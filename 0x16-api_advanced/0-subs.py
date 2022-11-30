#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    ''' get subscribers of SubReddit using API call '''
    client_id = 'g_3cI1hmYOJ-3wKE-UH-jw'
    secret_token = 'Sx2Uw-jmlVMz5rQ9Cu-hs1vXZfl81w'

    # client_id is 'personal use script' secret_token is 'token'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_token)

    # login method (password), username, and password
    data = {'grant_type': 'password',
            'username': 'lordzeus9000',
            'password': 'godofwar'}

    # setup header info
    headers = {'User-Agent': 'Mybot/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    # while the token is valid (~2 hours)
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

    r = "https://oauth.reddit.com/r/{}/about".format(subreddit)

    try:
        res = requests.get(r, headers=headers)
        return res.json().get('data').get('subscribers')
    except Exception as e:
        return 0
