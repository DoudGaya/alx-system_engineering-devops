#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and prints the titles of all hot posts listed
"""
import requests


def recurse(subreddit, hot_list=[]):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'My Agent 1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            if 'after' in data['data'] and data['data']['after'] is not None:
                after = data['data']['after']
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    else:
        return None
