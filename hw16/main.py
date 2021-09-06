from geolocation import get_address, generate_google_maps_url


if __name__ == '__main__':
    with open('coords.txt') as f:
        input_data = f.read().strip()
        input_data = input_data.replace('\'', '').replace(',', '.')

    lat, long = input_data.split(';')

    address = get_address(lat, long)
    google_maps_url = generate_google_maps_url(lat, long)

    print(f'Location: {address}')
    print(f'Goggle Maps URL: {google_maps_url}')
