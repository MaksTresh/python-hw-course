import os
from typing import Tuple

from exif import Image


def image_coordinates(image_path: str) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    with open(image_path, 'rb') as f:
        img = Image(f)

    coords = img.gps_latitude, img.gps_longitude
    return coords


def save_coords(lat: Tuple[float, float, float], long: Tuple[float, float, float]):
    with open('coords.txt', 'w') as f:
        coords = f'{lat[0]:.0f},{lat[1]:.0f}\';{long[0]:.0f},{long[1]:.0f}\''
        f.write(coords)


if __name__ == '__main__':
    lat, long = image_coordinates('./image.jpg')
    save_coords(lat, long)
    os.system('python ../hw16/main.py')
