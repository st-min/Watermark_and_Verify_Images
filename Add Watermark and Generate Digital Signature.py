import cv2 as cv
import numpy as np
import os
import random
import hashlib
from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Input and output directory paths
input_directory = "/path/to/input_directory"
output_directory = "/path/to/output_directory"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def calculate_average_brightness(img):
    return np.mean(cv.cvtColor(img, cv.COLOR_BGR2GRAY))

def add_noise_to_high_freq(img, noise_std):
    # Apply Laplacian filter to extract high-frequency components
    laplacian = cv.Laplacian(img, cv.CV_64F)

    # Generate noise
    noise = np.random.normal(0, noise_std, laplacian.shape)

    # Add noise to high-frequency components
    high_freq_noise = laplacian + noise

    # Adjust noise size to match original image channels
    if len(img.shape) == 3:  # For color images
        noise_shape = (high_freq_noise.shape[0], high_freq_noise.shape[1], 3)
    else:  # For grayscale images
        noise_shape = (high_freq_noise.shape[0], high_freq_noise.shape[1])

    # Crop high-frequency noise to match original image size
    high_freq_noise = high_freq_noise[:img.shape[0], :img.shape[1]]

    # Combine high-frequency noise with the original image
    img_with_noise = cv.addWeighted(img, 1, high_freq_noise.astype(np.uint8), 0.05, 0)

    return img_with_noise

def generate_signature(image_data):
    return hashlib.sha256(image_data).hexdigest()

# Process each file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Process only image files
        # Set image path
        image_path = os.path.join(input_directory, filename)
        # Open image
        img = cv.imread(image_path)
        # Error handling
        if img is None:
            print(f"Failed to load image: {image_path}")
            continue

        height, width = img.shape[:2]

        avg_brightness = calculate_average_brightness(img) # Calculate average brightness
        normalized_brightness = avg_brightness / 255.0  # Normalize brightness to 0-1
        noise_std = 0.3 + 3 * normalized_brightness       # Set noise std deviation proportional to normalized brightness (1-5)

        # Set random number of areas for Gaussian blur (16-64)
        num_areas = random.randint(16, 64)

        for _ in range(num_areas):
            # Select area for Gaussian blur
            distortion_area_size = int(0.03 * min(height, width))  # Select area size 3% of image size
            x1, y1 = np.random.randint(30, width - distortion_area_size - 30), np.random.randint(30,
                                                                                                 height - distortion_area_size - 30)
            x2, y2 = x1 + distortion_area_size, y1 + distortion_area_size

            # Select distorted area
            distorted_area = img[y1:y2, x1:x2]

            # Apply Gaussian blur (slight distortion)
            distorted_area = cv.GaussianBlur(distorted_area, (3, 3), 0)

            # Merge distorted area with the original image
            img[y1:y2, x1:x2] = distorted_area

        # Add noise to high-frequency parts
        img_with_noise = add_noise_to_high_freq(img, noise_std)

        # Save modified image
        output_path = os.path.join(output_directory, "distorted_" + filename)
        cv.imwrite(output_path, img_with_noise)

        # Generate and embed digital signature in image metadata
        with open(output_path, "rb") as f:
            image_data = f.read()
        signature = generate_signature(image_data)
        
        # Use PIL to add signature to image metadata
        pil_image = Image.open(output_path)
        meta = PngInfo()
        meta.add_text("Signature", signature)
        pil_image.save(output_path, pnginfo=meta)
