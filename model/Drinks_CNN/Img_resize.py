import os
import cv2

input_folder = "Images/coca_cola_images"
output_folder = "output_Img"
target_width = 224  # Common width
target_height = 224  # Common height

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process images
for root, _, files in os.walk(input_folder):
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(root, filename)
            output_path = os.path.join(output_folder, filename)

            # Read image
            image = cv2.imread(input_path)

            # Resize image
            resized_image = cv2.resize(image, (target_width, target_height))

            # Save preprocessed image
            cv2.imwrite(output_path, resized_image)

            print(f"Processed: {input_path} -> {output_path}")
