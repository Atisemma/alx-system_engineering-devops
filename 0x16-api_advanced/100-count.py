#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}

    if after:
        params['after'] = after

    user_agent = (
        "python:MyRedditScraper:v1.0 "
        "(by /u/YourRedditBot)"
    )
    headers = {'User-Agent': user_agent}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params
        )
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            for child in children:
                title = child['data']['title'].lower()
                for word in word_list:
                    if title.count(word.lower()) > 0:
                        counts[word.lower()] = (
                            counts.get(word.lower(), 0) +
                            title.count(word.lower())
                        )

            if data['data']['after']:
                return count_words(
                    subreddit,
                    word_list,
                    data['data']['after'],
                    counts
                )
            else:
                sorted_counts = sorted(
                    counts.items(),
                    key=lambda x: (-x[1], x[0])
                )
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            print("No posts match or the subreddit is invalid.")
    except requests.exceptions.RequestException:
        print("Error occurred while fetching data from Reddit API.")
