#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
 of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
      subreddit (str): The name of the subreddit.

    Returns:
      int: The number of subscribers for the subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)",
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data").get("children")
    for i in range(10):
        print(data[i].get("data").get("title"))
