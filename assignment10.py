"""
CIS206 W01 3/19/2024
Alexander Martinez Leyva
Assignment 10
"""

import requests
import json

# JSON data from the URL
url = "https://wikimedia.org/api/rest_v1/#/Pageviews%20data"
response = requests.get(url)

# Check the request (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Print the entire JSON data for debugging
    print(data)

    # Process the JSON data
    # iterate over each item in the JSON data
    for item in data['items']:
        # Print
        print(item)

        # Access article and views count
        if isinstance(item, dict):
            article = item.get('article')
            views = item.get('views')

            # the article and views count
            if article and views:
                print(article, views)
        else:
            print("Item is not a dictionary:", item)

    # Additional processing
else:
    print("Failed to fetch JSON data:", response.status_code)
