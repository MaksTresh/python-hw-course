from geopy import Nominatim


def get_address(lat: str, long: str) -> str:
    geocoder = Nominatim(user_agent='hw-task')
    address = geocoder.reverse(query=(lat, long)).address
    return address


def generate_google_maps_url(lat: str, long: str) -> str:
    return f'https://www.google.com/maps/search/?api=1&query={lat},{long}'
