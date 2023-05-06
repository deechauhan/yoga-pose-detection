"""Main camera launcher.

This launcher should be able to:
    1. Choose from multiple cameras
    2. Call any dependency to add overlay in realtime
"""
import cv2

cap = cv2.VideoCapture(0)  # type:ignore[call-arg]

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    ret, original_frame = cap.read()
    if not ret:
        print("Error: Could not read frame from camera")
        break

    # Mirror each frame
    mirrored_frame = cv2.flip(original_frame, 1)
    cv2.imshow("Yoga pose detection", mirrored_frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
