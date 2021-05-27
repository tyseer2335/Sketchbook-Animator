import cv2
import numpy as np
import glob  
import re
# Import essential libraries 
 
imgArray = [] # Array to store all images

def numericalSort(value): # Sorts frame by numerical value 
    parts = re.compile(r"(\d+)").split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts # return sorted frames so that frames are rendered in order
# https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/

print("Sketchbook Animator")  
print("Tyseer, 2021")
print("_________________________________")  
print("Now starting to stitch frames......") 
cv2.waitKey(10000) # Wait 10 seconds

for image in sorted(glob.glob("filteredImg/*.png") , key=numericalSort): # Loop through all images
    img = cv2.imread(image) # Read image
    height, width, layers = img.shape # Get height width and layers from the img object 
    size = (width,height) # Make the size of the video
    imgArray.append(img) # Append to the array  

out = cv2.VideoWriter("finalVideo.avi", cv2.VideoWriter_fourcc(*'DIVX'), 15, size) # Write the video 

for i in range(len(imgArray)): # Loop through the image array
    out.write(imgArray[i]) # Write each frame to the video  
    print("Stitched frame at " + str(i)) # Prints progress
out.release() # Release the video into root directory

