#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """ function that returns he number of subscribers """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0
    result = r.json()
    if 'data' not in result:
        return 0
    number_subscribers = result['data']['subscribers']
    return number_subscribers
