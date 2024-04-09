#!/usr/bin/python3
"""function that queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers)
for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ function that returns he number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, allow_redirects=False)

    if r.status_code != 200:
        return 0
    result = r.json()
    if 'data' not in result:
        return 0
    number_subscribers = result['data']['subscribers']
    return number_subscribers
