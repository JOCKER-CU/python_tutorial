import cv2

# Initialize video capture (0 for webcam, or use a video file path)
video = cv2.VideoCapture(0)

# Initialize the tracker
tracker = cv2.TrackerCSRT_create()

# Read the first frame
ret, frame = video.read()
if not ret:
    print("Failed to read video")
    video.release()
    exit()

# Select the region of interest (ROI) for tracking
roi = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
tracker.init(frame, roi)

while True:
    # Read a new frame
    ret, frame = video.read()
    if not ret:
        break

    # Update the tracker
    success, box = tracker.update(frame)

    if success:
        # Draw the tracked object
        x, y, w, h = map(int, box)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking failed", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Object Tracking", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
