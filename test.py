from pytube import YouTube


import numpy as np
import cv2
import os
import time

from multiprocessing import Pool
 
# where to save
SAVE_PATH = "./" #to_do
 
# link of the video to be downloaded
link="https://www.youtube.com/watch?v=GibiNy4d4gc"
 
try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error") #to handle exception
 
# filters out all the files with "mp4" extension
d_video = yt.streams.filter(progressive = True, file_extension = "mp4").first()
  
# get the video with the extension and
# resolution passed in the get() function
try:
    # downloading the video
    d_video.download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')

cam = None 
for f in os.listdir(SAVE_PATH):
    if ".mp4" in f:
        cam = cv2.VideoCapture(os.path.join(SAVE_PATH,f))
  
try:
      
    # creating a folder named data
    if not os.path.exists('./data'):
        os.makedirs('./data')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()

filenames = []
for f in os.listdir("./data"):
    filenames.append(os.path.join("./data",f))


def process(img_path):
    # Initialize the ORB detector algorithm
    if  isinstance(img_path, str):
      orb = cv2.ORB_create()
      
      # Now detect the keypoints and compute
      # the descriptors for the query image
      # and train image
      kp, des = orb.detectAndCompute(cv2.imread(img_path), None)
    else:
      for pa in image_path:
        orb = cv2.ORB_create()
        
        # Now detect the keypoints and compute
        # the descriptors for the query image
        # and train image
        kp, des = orb.detectAndCompute(cv2.imread(pa), None)

t1 = time.time()
for f in filenames:
    process(f)
t2 = time.time()
chunked_list = list()
chunk_size = int(len(filenames)/16)
for i in range(0, len(filenames), chunk_size):
    chunked_list.append(filenames[i:i+chunk_size])
print(t2-t1)
with Pool(16) as pool:
    pool.map(process, chunked_list)

t3 = time.time()
print(t3-t2)
