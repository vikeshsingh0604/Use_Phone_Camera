import cv2
import numpy as np

# Update with your actual IP camera URL
url = "Enter your webcam IP address"
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()  # Use ret to check if the frame was captured
    
    if ret:  # Check if the frame was successfully captured
        cv2.imshow("Frame", frame)
    else:
        print("Failed to grab frame")  # Optional: log if frame capture fails
    
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()
