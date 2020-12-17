import cv2
import numpy as np
#import request
import sys

# for laptop camera...!!

#faceCascade = cv2.CascadeClassifier(cascPath)

cam = cv2.VideoCapture(0)                               #live stream data
cv2.namedWindow("Screen Shot App...!!")
img_counter = 0
img_counter1 = 0

inp = input("Portrait or landscape or access mobile camera..?")

#for landscape image...

if inp == "L":

    while True:
        ret, imga = cam.read()

        if not ret:
            print("failed to grab frame..")
            break

        height, width = imga.shape[0:2]
        rotationMatrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1.0)
        rotatedImage = cv2.warpAffine(imga, rotationMatrix, (width, height))
        cv2.imshow("test", imga)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape Hit.. Closing the app...")
            break

        elif k % 256 == 32:
            img_name = "Landscape_{}.png".format(img_counter1)
            cv2.imwrite(img_name, rotatedImage)

            print("screen shot taken..")
            img_counter1 += 1

    cam.release()

    cam.destroyAllWindows()


#for portrait image...

elif inp == "P":

    while True:
        ret, frame = cam.read()
        frame = cv2.resize(frame, None, fx=1.0, fy=1.5, interpolation=cv2.INTER_AREA)
        if not ret:
            print("failed to grab frame..")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape Hit.. Closing the app...")
            break

        elif k % 256 == 32:
            img_name = "Portrait_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("screen shot taken..")
            img_counter += 1

    cam.release()

    cam.destroyAllWindows()

#for accessing front cam of the pc...
# Only works with an android phone...
# need to install ipweb cam for this application..
# get the url by opening the ip web cam and paste it here..
# elif inp == "M"
#     url = ""
#     while True:
#         img_resp = requests.get(url)
#         img_arr = np.array(bytearray(img_resp.content),dtype = np.uint8)
#         img = cv2.imdecode(img_arr, -1)
#         k = cv2.waitKey(1)
#         if k % 256 == 27:
#             print("Escape Hit.. Closing the app...")
#             break
#
#         elif k % 256 == 32:
#             img_name = "mobile_cam_{}.png".format(img_counter)
#             cv2.imwrite(img_name, frame)
#             print("screen shot taken..")
#             img_counter += 1

else:
    print("enter valid input..")



