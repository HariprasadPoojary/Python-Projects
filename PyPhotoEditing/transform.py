from image import Image
import numpy


def change_brightness(image, factor):
    # factor is a value  (0 < n > 1) to determine the brightness
    # (< 1 = darken, < 1 = brighten)
    x_pixels, y_pixels, num_channels = image.array.shape  # get dimension(x,y), channels
    # * make an empty image so that we don't modify the original
    new_image = Image(x_pixels, y_pixels, num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_image.array[x, y, c] = image.array[x, y, c] * factor

    return new_image


if __name__ == "__main__":
    note = Image(filename="lake.png")
    new_note = change_brightness(note, 1.7)
    new_note.write_image("new_lake.png")
