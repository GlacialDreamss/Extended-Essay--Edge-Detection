# Extended Essay: Edge Detection
 Images are cool
 Multiple implementations of edge detection for school
 I like school very much :P

 Instructions:
 - Generating results based on a dataset (see folders for examples)
 1. Rename your dataset to image(number).(extension) in increasing order from 0 and store it in the dataset folder
 2. In edgeDetection.py, for each line that contains the word image, change the file extension from .png to your desired one
 3. Run edgeDetection.py and your results should be stored in the other folders
 
 - The following are how to collate the data from your own results
 1. In fileCompare.py, for lines 13 to 16, change the ".png" to your desired extension
 2. Change the index of the for loop (second number on line 12) to the final number of your renamed dataset images + 1
 3. Run fileCompare.py, the results will be stored in byteAverage.csv as the following:
    - Row 1: Total Dataset bytes, Total Greyscale bytes, Total Sobel bytes, Total Canny bytes
    - Row 2: Average Dataset bytes, Average Greyscale bytes, Average Sobel bytes, Average Canny bytes
    - Row 3 (percentage of dataset left over for each category): Residual Canny bytes, Residual Sobel bytes, Residual greyscale bytes 
 

 Note - if you don't want coloured sobel results, like those in the sobel folder, change the "image" on line 25 of edgeDetection.py to "gray".

