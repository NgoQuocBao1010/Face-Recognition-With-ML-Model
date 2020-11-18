import numpy as np
import cv2
import glob
import os
# from mtcnn.mtcnn import MTCNN

path = 'uv\\Yawning\\*.*'

# resize image by giving the size in tuple: (new width, new height)
def resizeImage(image, coordinate=(0, 0)):
    try:
        width, height = coordinate
        image = cv2.resize(image, (width, height))
        return image
    except Exception as e:
        # print(str(e))
        return None

# transform image to black and white
def grayscaleImage(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray
    except Exception as e:
        # print(str(e))
        return None


def using_deep_learning(path):
    net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
    for file in glob.glob(path):
        videoName = file.split("\\")[2].split(".")[0]
        folder = videoName.split("-")[0]
        print(videoName)
        video = cv2.VideoCapture(file)
        with open('file.txt', 'a+') as f:
            f.write(videoName + '\n')

        count = 0
        i = 0
        while True:
            i += 1
            if cv2.waitKey(25) == 13:
                break

            ret, frame = video.read()

            if ret == False:
                break

            if i % 10 != 0:
                continue

            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
            net.setInput(blob)
            detections = net.forward()

            (h, w) = frame.shape[:2]

            # print(h, w)
        
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                if confidence < 0.4:
                    continue

                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                
                try:
                    frame = frame[startY:endY, startX:endX]
                    frame = grayscaleImage(frame)
                    frame = resizeImage(frame, (48, 48))
                    # cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
                    cv2.imshow('test', frame)
                    count += 1
                    cv2.imwrite(f'data\\{folder}\\{videoName}_' + str(count) + '.jpg', frame)
                except:
                    continue



# def detectFaceFromVideoDeepLearing()

using_deep_learning(path)
# uv\Yawning\15-MaleNoGlasses-Yawning.avi
# test("uv\\Yawning\\15-MaleNoGlasses-Yawning.avi")