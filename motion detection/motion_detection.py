import cv2
import numpy as np
from datetime import datetime

# Initialize video capture (0 for webcam, or provide a video file path)
video = cv2.VideoCapture(0)

# Variables to store the first frame and motion log
first_frame = None
motion_log = []

while True:
    # Read the current frame
    ret, frame = video.read()
    if not ret:
        break

    # Convert frame to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Initialize the first frame
    if first_frame is None:
        first_frame = gray
        continue

    # Compute the absolute difference between the first frame and the current frame
    frame_diff = cv2.absdiff(first_frame, gray)

# Ensure the threshold image is binary and of correct type
    _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)
    thresh = np.uint8(thresh)

# Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) < 1000:  # Ignore small areas
            continue
        motion_detected = True

        # Draw bounding boxes around motion regions
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Log motion events
    if motion_detected:
        motion_log.append(datetime.now())

    # Display the video feed
    cv2.imshow("Motion Detection", frame)
    cv2.imshow("Threshold", thresh)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()

# Print motion timestamps
print("Motion Detected at:")
for timestamp in motion_log:
    print(timestamp)
