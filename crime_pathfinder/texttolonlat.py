import requests

def geocode_address(api_key, address):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    # Prepare parameters for the API request
    params = {
        'address': address,
        'key': api_key,
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()

    # Check if the response contains valid results
    if data['status'] == 'OK':
        # Extract the coordinates from the first result
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        # Handle errors
        print(f"Geocoding API request failed with status: {data['status']}")
        return None

#api_key = 'AIzaSyB0OTXJmDBC3Al_FiDhMojWLK9F8Obm5x8'
#user_address = '1600 Amphitheatre Parkway, Mountain View, CA'

#coordinates = geocode_address(api_key, user_address)
#print(coordinates[0])