import urllib3
import json

BASE = "https://api.myl.cl"
PROFILE_ENDPOINT = "/cards/profile" # add <edition>/<card>
EDITION_ENDPOINT = "/cards/edition" # add <edition>

def client(method, endpoint):
    http_client = urllib3.PoolManager()

    response = http_client.request(method, f'{BASE}{endpoint}')
    data = json.loads(response.data.decode('utf-8'))

    return data

def get_edition_cards(edition_name):
    return client('GET', f'{EDITION_ENDPOINT}/{edition_name}')

def get_profiles_from_cards(cards):
    http = urllib3.PoolManager()
    with http.request('GET', BASE, preload_content=False) as r:
    # Check if the initial request was successful (status code 200)
        if r.status == 200:
            print("Initial request successful.")
            # Extract and print the response content
            print(r.data.decode('utf-8'))

            # Make additional requests within the same session
            for endpoint in ['/resource1', '/resource2', '/resource3']:
                url = BASE + endpoint
                # Make a GET request to each endpoint
                response = http.request('GET', url)
                
                # Check if the request was successful (status code 200)
                if response.status == 200:
                    print(f"Request to {url} successful:")
                    print(response.data.decode('utf-8'))
                else:
                    print(f"Error: Unable to fetch data from {url}. Status Code: {response.status}")
        else:
            print(f"Error: Unable to establish a connection. Status Code: {r.status}")
    
    # Close the pool connection
    http.clear()