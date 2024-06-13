import requests
import pandas as pd
import csv
from datetime import datetime

# Replace these with the repository owner and name
owner = 'jayly-bot'
repo = 'addons'

# GitHub API URL for repository releases
api_url = f'https://api.github.com/repos/{owner}/{repo}/releases'

# Send a GET request to the GitHub API
response = requests.get(api_url)
date = datetime.today().strftime('%Y-%m-%d')

# Check if the request was successful
if response.status_code == 200:
    releases = response.json()

    # List to hold the release data
    release_data = []

    # Iterate over the releases
    for release in releases:
        release_name = release['name']
        release_tag = release['tag_name']
        release_date = release['published_at']
        
        # Iterate over the assets of the release
        for asset in release['assets']:
            asset_name = asset['name']
            download_count = asset['download_count']
            
            # Append the data to the list
            release_data.append({
                'Release Name': release_name,
                'Tag Name': release_tag,
                'Published Date': release_date,
                'Asset Name': asset_name,
                'Download Count': download_count
            })

    # Convert the list to a DataFrame
    df = pd.DataFrame(release_data)

    # Write the DataFrame to a CSV file
    df.to_csv('github_release_downloads/ ' + date + '.csv', index=False)

    print('Data has been written to github_release_downloads/' + date + '.csv')
else:
    print(f'Failed to fetch releases: {response.status_code}')
