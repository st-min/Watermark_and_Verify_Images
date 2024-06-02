# Watermark and Verify Images

This project provides a tool to add watermarks to images and verify their integrity using digital signatures. The watermark is created by applying noise and Gaussian blur to parts of the image, and the integrity is verified by generating and checking digital signatures.

## Features

- Add watermark to images by applying Laplacian noise and Gaussian blur.
- Generate digital signatures for the watermarked images.
- Verify the integrity of watermarked images using the generated digital signatures.

## Requirements

- Python 3.x
- OpenCV
- NumPy

You can install the required Python packages using the following command:

```bash
pip install opencv-python-headless numpy
```

Usage

1. Add Watermark and Generate Digital Signature
This script reads images from the input directory, applies watermarking, and saves the watermarked images and their digital signatures in the output directory.


2. Verify Digital Signature
This script reads watermarked images and their digital signatures from the output directory, and verifies the integrity of the images by comparing the current and stored signatures.


Directory Structure

Copy code
.
├── watermark_and_verify_images
│   ├── add_watermark_and_generate_signature.py
│   ├── verify_signature.py
│   └── README.md


How to Run

Clone the repository.
Install the required Python packages.
Set the input and output directory paths in both scripts.
Run add_watermark_and_generate_signature.py to add watermarks and generate digital signatures.
Run verify_signature.py to verify the digital signatures of the watermarked images.
bash
Copy code
python add_watermark_and_generate_signature.py
python verify_signature.py
