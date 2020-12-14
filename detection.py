import cv2
import numpy as np

#cv2.CascadeClassifier.load('haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier('cascades\src\data\haarcascade_frontalface_alt2.xml')


cam = cv2.VideoCapture(0)                               #live stream data
cv2.namedWindow("Screen Shot App...!!")
img_counter1 = 0

while True:
    ret, imga = cam.read()

    gray = cv2.cvtColor(imga, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        # cv2.rectangle(imga, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = imga[y:y + h, x:x + w]

        img_name = "detected_{}.png".format(img_counter1)
        cv2.imwrite(img_name, roi_gray)

        color = (255,0,0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(imga, (x,y), (end_cord_x,end_cord_y), color, stroke)

        #display the image...
        cv2.imshow("test", imga)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape Hit.. Closing the app...")
            break

    cam.release()

    #cam.destroyAllWindows()


