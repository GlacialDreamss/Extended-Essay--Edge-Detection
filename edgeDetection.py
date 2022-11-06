import cv2 

# Sobel write
def sobel(image):
    sobel = cv2.Sobel(image,cv2.CV_64F,1,1,ksize=5)  # x,y: 1,1
    sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)  # x,y: 1,0
    sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)  # x,y: 0,1
    
    cv2.imwrite('sobel/image'+str(num)+".png", sobel)
    cv2.imwrite('sobelX/image'+str(num)+".png", sobelx)
    cv2.imwrite('sobelY/image'+str(num)+".png", sobely)


# Canny write
def canny(image):
    blur = cv2.GaussianBlur(image,(3,3),0) #No I didn't forget to make the blur 5x5 as I implied I would for the entire experiment and am not now salty smh
    canny = cv2.Canny(blur,0,50)

    cv2.imwrite('gaussian blur/image'+str(num)+".png", blur)
    cv2.imwrite('canny/image'+str(num)+".png", canny)


#Main loop
for num in range(0,100):
    
    # Universal variables
    rgb = cv2.imread('dataset/image'+str(num)+'.png')
    greyscale = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    
    #Calling canny and sobel for the entire dataset
    sobel(rgb)
    canny(rgb)

    #Writing grayscale
    cv2.imwrite('greyscale/image'+str(num)+'.png', greyscale)