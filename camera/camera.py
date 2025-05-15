# import cv2

# # Open the default camera
# cam = cv2.VideoCapture(0)

# # Get the default frame width and height
# frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

# while True:
#     ret, frame = cam.read()

#     # Write the frame to the output file
#     out.write(frame)

#     # Display the captured frame
#     cv2.imshow('Camera', frame)

#     # Press 'q' to exit the loop
#     if cv2.waitKey(1) == ord('q'):
#         break

# # Release the capture and writer objects
# cam.release()
# out.release()
# cv2.destroyAllWindows()
# import cv2
# import matplotlib.pyplot as plt

# # Open the camera
# cam = cv2.VideoCapture(0)

# while True:
#     ret, frame = cam.read()

#     if not ret:
#         break

#     # Convert the frame from BGR to RGB for matplotlib
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     plt.imshow(frame_rgb)
#     plt.axis('off')
#     plt.draw()
#     plt.pause(0.001)
#     plt.clf()  # Clear the plot for the next frame

#     # Press 'q' to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cam.release()
# plt.close()

import cv2

# Open the default camera
cam = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cam.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    # Capture each frame
    ret, frame = cam.read()

    # Check if frame was successfully captured
    if not ret:
        print("Error: Failed to capture the frame.")
        break

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()
