import argparse

from PIL import Image


def resize_image(input_image: str, output_image: str, scale: float):
    image = Image.open(input_image)
    width, height = image.size
    size = int(width * scale), int(height * scale)
    resized_image = image.resize(size)
    resized_image.save(output_image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for resizing an image with a given scale.')
    parser.add_argument('-i', '--input-image', dest='input_image', help='Input image', default='input.jpg')
    parser.add_argument('-o', '--output-image', dest='output_image', help='Output image', default='output.jpg')
    parser.add_argument('-s', '--scale', dest='scale', help='The scale of output image', default=0.5, type=float)
    args = parser.parse_args()

    if args.scale <= 0:
        print('The scale must be greater than zero')
        exit(2)

    resize_image(args.input_image, args.output_image, args.scale)
