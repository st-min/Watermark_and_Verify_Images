# 💧Watermark and Verify Images💧

This project provides a tool to add watermarks to images and verify their integrity using digital signatures. The watermark is created by applying noise and Gaussian blur to parts of the image, and the integrity is verified by generating and checking digital signatures embedded in the image metadata.

## Features

- Add watermark to images by applying Laplacian noise and Gaussian blur.
- Generate digital signatures for the watermarked images.
- Embed digital signatures in the image metadata.
- Verify the integrity of watermarked images using the embedded digital signatures.  

#### Make the intensity of the noise proportional to the normalized image brightness.
```python
avg_brightness = calculate_average_brightness(img)
normalized_brightness = avg_brightness / 255.0
noise_std = 0.3 + 3 * normalized_brightness

```
#### Gaussian blur was randomly added to the local part of the image in proportion to the image size.
```python
num_areas = random.randint(16, 64)

for _ in range(num_areas):
        distortion_area_size = int(0.03 * min(height, width))
        x1, y1 = np.random.randint(30, width - distortion_area_size - 30),
                        np.random.randint(30, height - distortion_area_size - 30)
        x2, y2 = x1 + distortion_area_size, y1 + distortion_area_size

        distorted_area = img[y1:y2, x1:x2]

        distorted_area = cv.GaussianBlur(distorted_area, (3, 3), 0)
```

## Method
### Digital Signature  
<img src="https://github.com/st-min/Watermark_and_Verify_Images/assets/70586865/8248f33b-fb72-4b4f-b542-7425614cd0b1" style="width: 40%; height: 40%;">

<img src="https://github.com/st-min/Watermark_and_Verify_Images/assets/70586865/c2ab25da-3f7e-463f-8e78-0ef99283e92c" style="width: 40%; height: 40%;">  [8]

## ⚙️Requirements

- Python 3.7
- OpenCV
- NumPy
- Pillow

You can install the required Python packages using the following command:

```bash
pip install opencv-python numpy Pillow
```

## Usage
I used image data from the cocodataset. http://cocodataset.org/#download
### 1. Add Watermark and Generate Digital Signature
This script reads images from the input directory, applies watermarking, saves the watermarked images, and embeds their digital signatures in the metadata.
(Add Watermark and Generate Digital Signature.py)


### 2. Verify Digital Signature
This script reads watermarked images from the output directory and verifies their integrity by comparing the current and stored signatures embedded in the image metadata. (Verify Digital Signature.py)

## Directory Structure

Copy code
.
├── watermark_and_verify_images  
│   ├── add_watermark_and_generate_signature.py  
│   ├── verify_signature.py  
│   └── README.md  


## How to Run 🏃🏻

    1. Clone the repository.
    2. Install the required Python packages.
    3. Set the input and output directory paths in both scripts.
    4. Run add_watermark_and_generate_signature.py to add watermarks and generate digital signatures embedded in the metadata.
    5. Run verify_signature.py to verify the digital signatures of the watermarked images.
    
`$ python add_watermark_and_generate_signature.py`  
`$ python verify_signature.py`


## Example 
<table align="center">
 <tr>
  <th>Original Image</th><th>Watermarked Image</th>
 </tr>
 <tr>
  <td>
   <img src="https://github.com/st-min/Watermarking_using_CNN_Digital_Signature/assets/70586865/6ab038a5-5673-4a49-a625-474961f23416" style="border-radius: 6px;">
  </td>
  <td>
    <img src="https://github.com/st-min/Watermarking_using_CNN_Digital_Signature/assets/70586865/722d0f68-7003-48c5-8dd7-21e3606dd435" style="border-radius: 6px;">
  </td>
</tr>
    </tr>
 <tr>
  <td>
   <img src="https://github.com/st-min/Watermarking_using_CNN_Digital_Signature/assets/70586865/50c69a37-d356-424f-b84a-8f7f623534fb" style="border-radius: 6px;">
  </td>
  <td>
    <img src="https://github.com/st-min/Watermarking_using_CNN_Digital_Signature/assets/70586865/64e3b41d-3736-4fd6-aac3-1a965dd8e9ae" style="border-radius: 6px;">
  </td>
</tr>
</table>
     
#### Output Verification Results
   ![image](https://github.com/st-min/Watermark_and_Verify_Images/assets/70586865/890607f4-2e68-4784-93a6-b546292c86fc)


## 🥅 Final Goal 🥅   
<table align="center">
 <tr>
  <th>System Achitechture Flowchart</th><th>Variication Step Flowchart</th>
 </tr>
 <tr>
  <td>
   <img src="https://github.com/st-min/Watermark_and_Verify_Images/assets/70586865/7d6a18df-798a-47e0-a405-97a08114afe8" style="width: 70%; height: 70%;">
  </td>
  <td>
    <img src="https://github.com/st-min/Watermark_and_Verify_Images/assets/70586865/5781b377-1ca2-44ab-adf4-04285093862f" style="border-radius: 6px;">
  </td>
 </tr>
</tr>
</table>

#### 1. Using CNN for Feature Extraction and Insertion
- CNNs can effectively learn complex patterns and features in images. By leveraging this, we can extract key features from the original image and determine where to insert the watermark. Using a CNN-based network, the watermark can be inserted into inconspicuous areas of the image, effectively hiding it while maintaining image quality.

#### 2. Enhancing Watermark Robustness with HiDDeN
- Adversarial Training: Using the structure of HiDDeN, we employ a Generator and Adversary to generate images with inserted watermarks and train the model to detect them. This process increases robustness, making it difficult to remove the watermark easily.

- Quality Preservation: Utilizing HiDDeN, we ensure that the watermark-inserted images are nearly indistinguishable from the original images, thus maintaining visual quality.

#### 3. Authentication and Verification Using Digital Signatures
- Digital Signature Generation: Before inserting the watermark, we generate a hash value of the image and encrypt it with a private key to create a digital signature. This digital signature is used to verify the integrity of the image.

- Verification Process: To verify whether the watermark-inserted image has been altered, we use the digital signature. For this, we validate the signature with the provided public key alongside the original image and confirm if the hash values match.

#### 4. Overall System Architecture
- Watermark Insertion: Using CNNs, we extract image features and insert the watermark in appropriate locations. By employing GANs, we maintain the quality of watermark-inserted images while increasing robustness. We generate a hash value of the image and encrypt it with a private key to create a digital signature.

- Watermark Detection and Verification: We decode the image to detect the watermark. Utilizing HiDDeN's Adversary, we verify the validity of the watermark. We verify the digital signature with the public key to ensure the image remains unchanged.

The combination of CNNs, HiDDeN, and digital signatures forms a robust and efficient digital watermarking system. Such a system would effectively protect the integrity of digital content and provide proof of ownership.

## Reference   
[1] Hannes Mareen, Lucas Antchougov, Glenn Van Wallendael, and Peter Lambert. " Blind Deep-Learning-Based Image Watermarking Robust Against Geometric Transformations." IEEE International Conference on Consumer Electronics (ICCE) 2024   
   
[2] Jung-hoe Hur, Seongmi Woo and Daewon Lee. "A Study on Audio Watermarking based on Deep Learning." 한국정보처리학회 학술대회논문집, vol. 29, no. 1, pp. 153-156, 2022.
   
[3] Tai, Le & Thanh, Ta. “Digital Image Watermarking Algorithm Using Blockmarking Technique for Copyright Protection.” 1-4. 10.1109/KSE59128.2023.10299411.
   
[4] Awasthi, Divyanshu & Tiwari, Anurag & Khare, Priyank & Srivastava, Vinay. “A comprehensive review on optimization-based image watermarking techniques for copyright protection.” Expert Systems with Applications 2023 
   
[5] 추형석. “적대적 생성신경망(Generative Adversarial Network)의 소개와 활용 현황.” 소프트웨어정책연구소   
   
[6] Zhu, Jiren & Kaplan, Russell & Johnson, Justin & Fei-Fei, Li. “HiDDeN: Hiding Data With Deep Networks.” 2018   
   
[7] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton. 2017. ImageNet classification with deep convolutional neural networks. Commun. ACM 60, 6 (June 2017), 84–90.   
  
[8] 우찬일, 구은희. (2020). “RSA와 해시 함수 기반 이미지 무결성 검증에 관한 연구.” 한국산학기술학회 논문지, 21(11), 878-883.  
