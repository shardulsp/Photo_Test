# this project is using mobile net ssd which is one of the best method now to detect object..
#for this we would need to download the frozen_inference_graph.pb and ssd_mobilenet.pbtxt...
import cv2

img = cv2.imread("girl1.jpeg")

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph (2).pb'
try:
    net = cv2.dnn_DetectionModel(weightsPath, configPath)
except Exception as e:
    print(e)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


classIds, confs, bbox = net.detect(img, confThreshold=0.5)
#print(classIds, bbox)

for classId, confidence, box in (classIds.flatten(),confs.flatten(),bbox):
    cv2.rectangle(img, box, color=(0,255,0), thickness=2)
    cv2.putText(img, classNames[classId-1].upper(),(box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)




cv2.imshow("image",img)


cv2.waitKey(0)

