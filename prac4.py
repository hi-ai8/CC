import requests 
# Replace with your actual API key and Search Engine ID 
API_KEY = 'AIzaSyBQFO_fbQJgm21XQSoH3EL_F8HQzIkQG-E' 
SEARCH_ENGINE_ID = '13cd45fc170c948ed' 
search_query = 'flux ai'
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
    print("No results found.")