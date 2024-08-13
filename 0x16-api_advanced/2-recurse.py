#!/usr/bin/python3
"""
function that queries the Reddit API and returns 
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should return None.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Get the number of subscribers for a given subreddit.

    Args:
      subreddit (str): The name of the subreddit.
      hot_list (list): List of hot articles.
      after (str): The next page.

    Returns:
      list: List of hot articles.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)",
    }
    params = {
        "limit": 100,
        "after": after,
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
