#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def json_find(d, key):
    """ prints to 10 hot subreddits """
    if isinstance(d, dict):
        if key in d.keys():
            print(d.get(key, "None"))
        [json_find(d[k], key) for k in d.keys()]

    elif isinstance(d, list):
        for item in d:
            json_find(item, key)
    else:
        pass


def top_ten(subreddit):
    """ return top ten hot posts"""
    if subreddit is None or type(subreddit) is not str:
        print("None")

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced: project: v1.0.0 \
               (by /u/lordzeus9000)'}
    try:
        hot_lists = requests.get(url, headers=headers)
        hot_lists.raise_for_status()
    except requests.exceptions.RequestException:
        print('None')
    json_find(hot_lists.json(), 'title')
