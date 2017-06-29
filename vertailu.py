import numpy as np
import cv2
from matplotlib import pyplot as plt

orb = cv2.ORB_create()

img1 = cv2.imread('haisuli.jpg',0)
img2 = cv2.imread('haisuli2.jpg',0) 

keypoints1, des1 = orb.detectAndCompute(img1,None)
keypoints2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)

img3 = cv2.drawMatches(img1,keypoints1,img2,keypoints2,matches[:10],None, flags=2)

plt.imshow(cv2.cvtColor(img3,cv2.COLOR_BGR2RGB))
plt.imsave('vertailu1.jpg', img3)
