#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests
import re
from collections import Counter


def count_words(subreddit, word_list):
    """
    Recursive function counting occurrences of keywords in Reddit

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to search for.

    Returns:
        None
    """
    # Set the API endpoint URL
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set the headers to avoid being blocked by Reddit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Make the API request
    try:
        response = requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()

        # Extract the titles of the hot posts
        titles = [
            post['data']['title'].lower() for post in data['data']['children']
        ]

        # Count the occurrences of the keywords
        word_counts = Counter()
        for title in titles:
            for word in word_list:
                # Use a regular expression to match the keyword
                pattern = r'\b' + re.escape(word.lower()) + r'\b'
                word_counts[word.lower()] += len(re.findall(pattern, title))

        # Print the sorted results
        for w, c in sorted(word_counts.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word}: {count}")
    else:
        # If the subreddit is invalid or no results are found, do nothing
        pass
