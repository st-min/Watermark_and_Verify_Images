# Watermark and Verify Images

This project provides a tool to add watermarks to images and verify their integrity using digital signatures. The watermark is created by applying noise and Gaussian blur to parts of the image, and the integrity is verified by generating and checking digital signatures embedded in the image metadata.

## Features

- Add watermark to images by applying Laplacian noise and Gaussian blur.
- Generate digital signatures for the watermarked images.
- Embed digital signatures in the image metadata.
- Verify the integrity of watermarked images using the embedded digital signatures.

## Method
![image](https://github.com/st-min/Watermark_and_Verify_Images/assets/70586865/1f7cd709-f4a6-40ae-95de-848a031c7a14)

## Requirements

- Python 3.7
- OpenCV
- NumPy
- Pillow

You can install the required Python packages using the following command:

```bash
pip install opencv-python-headless numpy Pillow
```

## Usage

# 1. Add Watermark and Generate Digital Signature
This script reads images from the input directory, applies watermarking, saves the watermarked images, and embeds their digital signatures in the metadata.
(Add Watermark and Generate Digital Signature.py)

# 2. Verify Digital Signature
This script reads watermarked images from the output directory and verifies their integrity by comparing the current and stored signatures embedded in the image metadata. (Verify Digital Signature.py)

##Directory Structure

Copy code
.
├── watermark_and_verify_images  
│   ├── add_watermark_and_generate_signature.py  
│   ├── verify_signature.py  
│   └── README.md  


## How to Run

    1. Clone the repository.
    2. Install the required Python packages.
    3. Set the input and output directory paths in both scripts.
    4. Run add_watermark_and_generate_signature.py to add watermarks and generate digital signatures embedded in the metadata.
    5. Run verify_signature.py to verify the digital signatures of the watermarked images.
    

        python add_watermark_and_generate_signature.py
        python verify_signature.py 


## Example
original image   
![image](https://github.com/st-min/Watermarking_using_CNN_Digital_Signature/assets/70586865/6ab038a5-5673-4a49-a625-474961f23416)   
embeded image   
![image](https://github.com/st-min/Watermarking_using_CNN_Digital_Signature/assets/70586865/722d0f68-7003-48c5-8dd7-21e3606dd435)   

original image   
![image](https://github.com/st-min/Watermarking_using_CNN_Digital_Signature/assets/70586865/50c69a37-d356-424f-b84a-8f7f623534fb)

embeded image   
![image](https://github.com/st-min/Watermarking_using_CNN_Digital_Signature/assets/70586865/64e3b41d-3736-4fd6-aac3-1a965dd8e9ae)




