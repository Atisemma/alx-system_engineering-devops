#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests
import re


def count_words(subreddit, word_list, hot_list=[], after=None, word_counts={}):
    """
    Recursive function that queries the Reddit API, parses the titles of all
    hot articles and prints a sorted count of given case-insensitive keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditAPIPython/0.1"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]
            after = data["data"]["after"]
            for post in posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    count = len(re.findall(r'\b{}\b'.format(word.lower()),
                                           title))
                    word_counts[word.lower()] = word_counts.get(
                        word.lower(), 0) + count
                hot_list.extend([post["data"]["title"]
                                for _ in range(count)])

            if after is not None:
                return count_words(subreddit, word_list, hot_list,
                                   after, word_counts)
            else:
                sorted_counts = sorted(
                    [(count, word) for word, count in word_counts.items()],
                    reverse=True)
                for count, word in sorted_counts:
                    if count > 0:
                        print("{}: {}".format(word, count))
        except (KeyError, ValueError):
            pass
    else:
        pass
