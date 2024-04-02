import base64

# Read the image file
with open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Final Year\\FYP\\FYP_Impl\\ColourSense\\facer\\image.jpg", "rb") as image_file:

    # Convert binary image data to base64-encoded string
    base64_encoded_image_data = base64.b64encode(image_file.read()).decode()

# Print or use the base64-encoded image data
print(base64_encoded_image_data)