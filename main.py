import cv2
import numpy as np


def rle_encode(data):
    encoding = []
    prev_value = data[0]
    count = 0

    for value in data:
        if value == prev_value:
            count += 1
        else:
            encoding.extend([prev_value, count])
            prev_value = value
            count = 1
    # Add the last set of values
    encoding.extend([prev_value, count])
    return encoding


def compress_image_with_rle(image_path, output_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    if image is None:
        print(f"Failed to load the image from {image_path}")
        return

    # Flatten the image pixels for RLE encoding
    pixels = image.flatten()

    # Apply RLE compression
    compressed_data = rle_encode(pixels)

    # Save the compressed data as a numpy file
    np.save(output_path, compressed_data)
    print(f"Compressed data saved to {output_path}.npy")


# Example usage
input_image_path = r'C:\Users\Mustafa.Ahmed\PycharmProjects\PythonProject3\black.jpg'  # Input image path
compressed_data_path = r'C:\Users\Mustafa.Ahmed\PycharmProjects\PythonProject3\compressed_data'  # Path to save compressed data

# Compress the image
compress_image_with_rle(input_image_path, compressed_data_path)
