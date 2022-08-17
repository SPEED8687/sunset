import cv2
import os
path="PRO-105-Reference-Code-Student-Activity-main/Images"
images=[]
allImages=os.listdir(path)
for eachImage in allImages:
    filename=path+'/'+eachImage
    images.append(filename)
frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
newVideo=cv2.VideoWriter('sunset.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for eachImage in images:
    frame=cv2.imread(eachImage)
    newVideo.write(frame)
newVideo.release()