import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('demo_strand.mp4')


# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

def getFrame(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)

    hasFrames,image = cap.read()
    #if hasFrames:
        #cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1/25 #//it will capture image 25fps
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

print(count-1)
# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

