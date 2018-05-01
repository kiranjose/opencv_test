import cv2
while True:
    cap=cv2.VideoCapture('http://192.168.1.135:8080/?action=stream')
    ret, image_np=cap.read()
    cv2.imshow('object detection', cv2.resize(image_np, (800,600)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
