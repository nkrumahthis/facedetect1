import cv2
import numpy

# create a cascadeclassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("im1.jpeg")
imgray = cv2.imread("im1.jpeg", 0)

# g
faces = face_cascade.detectMultiScale(imgray, scaleFactor = 1.05, minNeighbors = 5)

for x,y,w,h in faces:
    imgfaced = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

print(type(faces))

cv2.imshow("image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()