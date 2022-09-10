import numpy as np
import cv2 
from matplotlib import pyplot as plt

# Sobel write
def sobel(gray):
    sobel = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)  # x,y: 1,1

    cv2.imwrite('sobel/image'+str(num)+".png", sobel) 

# Canny write
def canny(gray):
    blur = cv2.GaussianBlur(gray,(3,3),0)
    canny = cv2.Canny(blur,0,200)

    cv2.imwrite('canny/image'+str(num)+".png", canny) 

#Main loop
for num in range(0,4):
    
    # Universal variables
    image = cv2.imread('dataset/image'+str(num)+'.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Calling canny and sobel for the entire dataset
    sobel(gray)
    canny(gray)

    #Writing grayscale
    cv2.imwrite('greyscale/image'+str(num)+'.png', gray)
