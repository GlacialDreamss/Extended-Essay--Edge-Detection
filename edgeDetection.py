import numpy as np
import cv2 

# Sobel write
def sobel(gray):
    sobel = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)  # x,y: 1,1
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)  # x,y: 1,0
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)  # x,y: 0,1
    
    cv2.imwrite('sobel/image'+str(num)+".png", sobel)
    cv2.imwrite('sobelX/image'+str(num)+".png", sobelx)
    cv2.imwrite('sobelY/image'+str(num)+".png", sobely)


# Canny write
def canny(gray):
    blur = cv2.GaussianBlur(gray,(3,3),0)
    canny = cv2.Canny(blur,0,50)

    cv2.imwrite('canny/image'+str(num)+".png", canny) 

#Main loop
for num in range(0,100):
    
    # Universal variables
    image = cv2.imread('dataset/image'+str(num)+'.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Calling canny and sobel for the entire dataset
    sobel(image)
    canny(image)

    #Writing grayscale
    cv2.imwrite('greyscale/image'+str(num)+'.png', gray)
