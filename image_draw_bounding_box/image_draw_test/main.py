import cv2
import numpy as np

# Load image
image = cv2.imread(r"C:\Users\hanna\Downloads\multiple-tables-1.jpeg")  # Update with your image path

# Define points (Ensure they are in the correct order)
points = np.array([[309,23],[1007,23],[309,125],[1007,125]], np.int32)

# Reshape points for polylines
points = points.reshape((-1, 1, 2))

# Draw bounding polygon
cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

# Show image
cv2.imshow("Bounding Box", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

