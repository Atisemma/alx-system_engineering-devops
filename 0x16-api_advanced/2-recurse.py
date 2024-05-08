#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}

    if after:
        params['after'] = after

    user_agent = "PythonRedditScraper/1.0"
    headers = {'User-Agent': user_agent}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            new_list = [child['data']['title'] for child in children]

            if new_list:
                hot_list.extend(new_list)
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list if hot_list else None
        else:
            return None
    except requests.exceptions.RequestException:
        return None
