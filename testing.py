import requests

url = 'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=c6f482bf-bf0f-4960-8b2f-9982c211addd'
response = requests.get(url)
d = response.json()
print(d)
