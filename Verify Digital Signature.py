import hashlib
from PIL import Image

def generate_signature(image_data):
    return hashlib.sha256(image_data).hexdigest()

def verify_signature(image_path):
    pil_image = Image.open(image_path)
    stored_signature = pil_image.info.get("Signature")

    with open(image_path, "rb") as f:
        image_data = f.read()

    current_signature = generate_signature(image_data)
    
    return stored_signature == current_signature

# Output directory path
output_directory = "/path/to/output_directory"

# Verify signatures for each file in the directory
for filename in os.listdir(output_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Process only image files
        # Set image path
        image_path = os.path.join(output_directory, filename)

        if verify_signature(image_path):
            print(f"Signature verified for {image_path}")
        else:
            print(f"Signature verification failed for {image_path}")
