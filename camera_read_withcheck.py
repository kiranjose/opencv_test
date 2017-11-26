import numpy as np
import cv2

device = 0
cap = cv2.VideoCapture(0)
# if capture failed to open, try again
if not cap.isOpened():
    cap.open(device)

# only attempt to read if it is opened
if cap.isOpened:
    while True:
        re, img = cap.read()
        # Only display the image if it is not empty
        if re:
            cv2.imshow("video output", img)
        # if it is empty abort
        else:
            print( "Error reading capture device")
            break
        k = cv2.waitKey(10) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Failed to open capture device")
