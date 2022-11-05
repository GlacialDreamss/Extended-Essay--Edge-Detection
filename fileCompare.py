import os
import csv

file = open("byteAverage.csv","w",newline='')
csvWrite = csv.writer(file)

dBytes = 0
sBytes = 0
cBytes = 0
gBytes = 0 

for num in range(0,4):
    dBytes += os.stat('dataset/image'+str(num)+'.png').st_size
    sBytes += os.stat('sobel/image'+str(num)+'.png').st_size
    cBytes += os.stat('canny/image'+str(num)+'.png').st_size
    gBytes += os.stat('greyscale/image'+str(num)+'.png').st_size

cBpercent = (cBytes/dBytes)*100
sBpercent = (sBytes/dBytes)*100
gBpercent = (gBytes/dBytes)*100

csvWrite.writerow([str(dBytes),str(gBytes),str(sBytes),str(cBytes)]) # Total bytes per test in a category

csvWrite.writerow([str(round(dBytes/(num+1))),str(round(gBytes/(num+1))),str(round(sBytes/(num+1))),str(round(cBytes/(num)+1))]) # Average bytes per test in a category

csvWrite.writerow([str(round(cBpercent)),str(round(sBpercent)),str(round(gBpercent))]) # Percentage of bytes leftover per test relative to the original dataset

file.close()