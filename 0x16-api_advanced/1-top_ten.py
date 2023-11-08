#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'My Agent 1'}
    params = {"limit": 10, }
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("None")
    else:
        print("None")
