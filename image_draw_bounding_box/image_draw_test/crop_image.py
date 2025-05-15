from PIL import Image

# Load the image
image = Image.open(r"C:\Users\hanna\Downloads\sales-invoice3.png")
# image = Image.open(r"C:\Users\hanna\Downloads\invoice4.png")

# Bounding box values (left, upper, right, lower)
# bbox = (0, 358, 1119, 1264)  # Example values
# bbox = (25, 10, 956, 178)  # Example values
# bbox = (25, 178, 956, 729)  # Example values
bbox = (50, 176, 819, 688)  # Example values

# Crop the image using the bounding box
cropped_image = image.crop(bbox)

# Convert RGBA to RGB if the image has an alpha channel
if cropped_image.mode == 'RGBA':
    cropped_image = cropped_image.convert('RGB')

# Save or display the cropped image
cropped_image.save('cropped_image13.jpg')
cropped_image.show()