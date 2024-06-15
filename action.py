import requests
import pandas as pd
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

# List to hold the release data
release_data = []

repos = [
    { 'owner': 'jayly-bot', 'repo': 'addons' },
    { 'owner': 'jaylydev', 'repo': 'terminator' },
    { 'owner': 'jaylydev', 'repo': 'nbt-to-mcstructure' },
    { 'owner': 'jaylydev', 'repo': 'interpreter' }
]

for repometa in repos:
    owner = repometa['owner']
    repo = repometa['repo']
    
    # GitHub API URL for repository releases
    api_url = f'https://api.github.com/repos/{owner}/{repo}/releases'

    # Send a GET request to the GitHub API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        releases = response.json()

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
                    'Owner': owner,
                    'Repo': repo,
                    'Release Name': release_name,
                    'Tag Name': release_tag,
                    'Published Date': release_date,
                    'Asset Name': asset_name,
                    'Download Count': download_count
                })
    else:
        print(f'Failed to fetch releases: {response.status_code}')


# Convert the list to a DataFrame
df = pd.DataFrame(release_data)

# Write the DataFrame to a CSV file
df.to_csv('github_release_downloads/ ' + date + '.csv', index=False)

print('Data has been written to github_release_downloads/' + date + '.csv')