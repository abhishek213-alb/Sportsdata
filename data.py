import requests
import pandas as pd
import json

{“api_key”: “paste_your_actual_api_key_here”}
def get_keys(path):
    with open(path) as f:
        return json.load(f)
        keys = get_keys("/Users/{your_username}/.secret/api_football.json")
api_key = keys['api_key']
rl = "https://api-football-v1.p.rapidapi.com/v2/leagues/seasonsAvailable/524"
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }
resp = requests.request("GET", url, headers=headers)
resp.status_code == requests.codes.ok
print(resp.text)

resp.json().keys()
resp.json()['api'].keys()
# Create dictionary of results for 'leagues' key
leagues_dict = resp.json()['api']['leagues']

# Visualize df for all English Premier league seasons available
leagues_df = pd.DataFrame.from_dict(leagues_dict)
display(leagues_df)
