#!/usr/bin/python3
""" returns number of hot articlesand prints a sorted count """
import requests
import re


def count_words(subreddit, word_list, after=None, word_counts=None):
    """ returns number of hot articlesand prints a sorted count """
    if word_counts is None:
        word_counts = {}
    if after is None:
        after = ''
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/your_username)'}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word in title:
                        if re.search(r'\b' + re.escape(word) + r'\b', title):
                            word_counts[word] = word_counts.get(word, 0) + 1

            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, word_counts)
            else:
                sorted_word_counts = sorted(word_counts.items(),
                                            key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_counts:
                    print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
