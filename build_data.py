import requests
from collections import defaultdict
import json


list_url = 'https://golab-indigo-data-store.herokuapp.com/app/api1/project'


r = requests.get(list_url)
list_data = r.json()

output =  defaultdict(int)

for list_data_project in list_data['projects']:
    if list_data_project['public']:
        print("PROJECT {}".format(list_data_project['id']))
        r = requests.get('https://golab-indigo-data-store.herokuapp.com/app/api1/project/' + list_data_project['id'])
        project_data = r.json()
        for location_data in project_data['project']['data'].get('delivery_locations', []):
            country = location_data.get('location_country',{}).get('value', '').strip()
            if country:
                output[country] += 1

with open('data.json', 'w') as fp:
    json.dump(output, fp, indent=4, sort_keys=True)
