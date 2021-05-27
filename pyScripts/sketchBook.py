import cv2 
import numpy as np 
import os 
# Import essential libraries 

def makeSketch(frame): # Function for doing the sketch effect
    img = cv2.imread(frame) # Read the frame
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converts the image to grey scale
    imgInvert = cv2.bitwise_not(imgGray) # Inverts the pixels (gets the negative image)
    imgSmoothing = cv2.GaussianBlur(imgInvert, (21, 21) ,sigmaX=0, sigmaY=0)  # Blurs the image
    return imgGray, imgSmoothing # Returns the greyed image and the image with the Gaussian Blur

def imgDodge(greyScale, blur):
     # Image Doge between the grey image and the blured image to produce a sketch effect
    return cv2.divide(greyScale, 255 - blur, scale = 256) 

# https://www.askaswiss.com/2016/01/how-to-create-pencil-sketch-opencv-python.html

print("Sketchbook Animator")  
print("Tyseer, 2021")
print("_________________________________") 

fileCount = 0 # Our file count (set as 0 to start)
for base, dirs, files in os.walk("frames"): # Loop through files and directories in frames folder
    for Files in files: # Loop through the files in frames
        fileCount += 1 # Increment fileCount by 1 each time we see a file
print("Total number of frames", fileCount) # Print total number of files  
print("_________________________________") 
print("Now starting to process frames.......") 
cv2.waitKey(10000) # Wait 10 seconds

try: 
    if not os.path.exists("filteredImg"): # If no directory named filteredImg exists
        os.makedirs("filteredImg") # Make a directory called filteredImg
except OSError: # If we cant make filteredImg
    print ("Error: Creating directory for filteredImg") # Print an error

for i in range(0, fileCount): # Loop from 0 to max frame number or the total file count
    imgGray, imgSmoothing = makeSketch("frames/frame" + str(i) + ".png")
    finalImg = imgDodge(imgGray, imgSmoothing)  

    cv2.imwrite(os.path.join("filteredImg" , "filteredImg"+ str(i) + ".png"), finalImg) 
        # Save the image into the filteredImg directory, name it as filteredImg(#).png
    print("Processed frame number " + str(i)) # Print what frame has been processed in the console

print("Successfully processed all " + str(fileCount) + " frames") 
cv2.destroyAllWindows() # Close Windows after we are done running script








