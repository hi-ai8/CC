import requests

# Replace with your actual API key and Search Engine ID
API_KEY = 'AIzaSyAHKWaVFmHOw0yCGMqVRnDOSDE0Vz_TpnQ'
SEARCH_ENGINE_ID = '814971251803240f8'

search_query = 'w3school'
url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q': search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID
}

response = requests.get(url, params=params)
results = response.json()

if 'items' in results:
    # print(results['items'][0]['link'])
    for item in results['items']:
        print(item['link'])
else:
    print("No results found.")
