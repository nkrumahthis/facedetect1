import cv2
import numpy

# create a cascadeclassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

capture = cv2.VideoCapture(0)

while 1:
    # capture frame by frame
    frame = capture.read()[1]

    # operation on the frame
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayframe, scaleFactor = 1.05, minNeighbors = 5)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("image", frame)
    if (cv2.waitKey(1)) & 0xFF == ord('q'): 
        break

capture.release()
cv2.destroyAllWindows()