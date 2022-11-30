#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests

def json_find(d, key):
    if isinstance(d, dict):
        if key in d.keys():
            return d.get(key)
        return "".join([ json_find(d[k],key) for k in d.keys() ])
    elif isinstance(d, list):
        return "".join([ json_find(x,key) for x in d ])
    else:
        return ""


def top_ten(subreddit):
    """ return top ten hot posts"""

    if subreddit is None or type(subreddit) is not str:
        return 0

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    hot_lists = requests.get(url,
                            headers={'User-Agent':
                            '0x16-api_advanced:project:\
                            v1.0.0 (by /u/lordzeus9000)'}).json()
    if 'title' in hot_lists.keys():
        return hot_lists.get('title')
    for key in hot_lists.keys():
        print(json_find(hot_lists[key], 'title'))
        