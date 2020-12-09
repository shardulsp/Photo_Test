import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("Screen Shot App...!!")
img_counter = 0
img_counter1 = 0

inp = input("Portrait or landscape?")

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
            img_name = "opencv_frame123_{}.png".format(img_counter1)
            cv2.imwrite(img_name, rotatedImage)

            print("screen shot taken..")
            img_counter1 += 1

    cam.release()

    cam.destroyAllWindows()

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
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("screen shot taken..")
            img_counter += 1

    cam.release()

    cam.destroyAllWindows()

else:
    print("enter valid input..")


