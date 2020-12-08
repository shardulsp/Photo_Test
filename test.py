import cv2
cam = cv2.VideoCapture(0)

cv2.namedWindow("Screen Shot App...!!")

img_counter = 0

#cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
#cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

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
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("screen shot taken..")
        img_counter += 1

cam.release()

cam.destroyAllWindows()