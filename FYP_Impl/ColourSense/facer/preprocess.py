
import os
import shutil
import functions as f  # Import the functions module


koln50_dataset_dir = 'C:/Users/ASUS/OneDrive/Desktop/FinalYear/FYP/Colorinsight-main/ColourSense/facer/koln50'  # Replace with the path to your Lapa dataset directory
koln50_preprocessed_dir = 'koln50_preprocessed'  # Directory to store preprocessed images

# Create directory structure for the preprocessed dataset
# os.makedirs(os.path.join(koln50_preprocessed_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(koln50_preprocessed_dir, 'test'), exist_ok=True)


# Preprocess test subset
test_dir = os.path.join(koln50_dataset_dir, 'test')
for class_dir in os.listdir(test_dir):
    class_path = os.path.join(test_dir, class_dir)
    if os.path.isdir(class_path):
        # Create class directory in preprocessed folder
        preprocessed_class_dir = os.path.join(koln50_preprocessed_dir, 'test', class_dir)
        os.makedirs(preprocessed_class_dir, exist_ok=True)
        for file in os.listdir(class_path):
            if file.endswith('.jpg'):
                # Extract face skin mask using save_skin_mask function
                image_path = os.path.join(class_path, file)
                skin_mask_image = f.save_skin_mask(image_path, preprocessed_class_dir)
                # # Check if the image was saved successfully before copying
                # if skin_mask_image is not None:
                #     # Save the preprocessed image in test directory
                #     shutil.copy(skin_mask_image, preprocessed_class_dir)