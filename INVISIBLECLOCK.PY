import cv2, os, time
import numpy as np

rawvideo = cv2.VideoCapture(0)
time.sleep = 1
count = 0
background = 0

for i in range(60):
    ret, frame = rawvideo.read() #start capturing frames
    print(ret)
    if not ret:
        continue #if not able to capture current frame, move to next
frame = np.flip(frame, axis=1)
