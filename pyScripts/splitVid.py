import cv2
import numpy as np
import os
# Import essential libraries 

print("Sketchbook Animator") 
print("Tyseer, 2021")
print("_________________________________")   
print("Now starting to split video.......")  
cv2.waitKey(10000) # Wait 10 seconds

fileCount = 0 # Sets variable for keeping track of file count in videos directory
for base, dirs, video in os.walk("video"): # Loop through files and directories in video folder
    for videos in video: # Loop through the files in video directory
        fileCount += 1  # Increment file count
        if fileCount > 1: # If we have more than 1 file
            print("Error: More than 1 files in video directory") # Error
            exit() # Exit program
        else: # We have 1 file
            cap = cv2.VideoCapture("video/" + str(os.listdir("video")[0])) # Play first file in video directory

try: # If a directory called frames is not made make one
    if not os.path.exists("frames"): # If frames doesent exist make one
        os.makedirs("frames") # Make the directory called frames
except OSError: # When an OS error occurs
    print ("Error: Creating directory of frames") # Print the error

currentFrame = 0 # Counter for frame number
while(True): # Keep going through entire video
    ret, frame = cap.read() # Capture frame by frame
    try: # Try this code
        name = "./frames/frame" + str(currentFrame) + ".png" # Saves image of the current frame as a .png file
        print ("Creating " + "Frame " +str(currentFrame)) # Prints the frame its creating
        cv2.imwrite(name, frame) # Saves frames into the directory    
        currentFrame += 1 # To stop duplicate image names 
    except cv2.error: # When we get a cv.2 error (meaning that no more frames in video)
        print("Completed Successfully, created " + str(currentFrame) + " frames")   
        cap.release() # When everything done, release the capture
        cv2.destroyAllWindows() # Close Windows after we are done running script 
        exit() # Exit program


