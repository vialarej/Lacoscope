#!/usr/bin/env python
# coding: utf-8

# In[73]:


import cv2
import matplotlib.pyplot as plt 
import math
from math import *
import numpy as np

from skimage.measure import label, regionprops, regionprops_table
from skimage.transform import rotate
import skimage.io as io


# In[77]:


disque = cv2.imread('./disque.png') 

def image(img) :
    print('dimensions :', img.shape)
image(disque)
plt.imshow(disque)


# In[78]:


def diametre(img):
    color_img=img.sum(axis=2)
    whites = np.sum(color_img>0) #compte le nombre de pixels pas noirs
    print('nombre de pixels :', whites)
    d = sqrt(whites/pi)*2
    print('diamètre :',d)
    return whites, d
diametre(disque)


# In[103]:


# test avec une image en conditions réelles 

from skimage.morphology import (square, rectangle, diamond, disk, octagon, star)
from skimage.morphology import erosion, dilation, opening, closing, white_tophat, black_tophat, reconstruction

plancton = cv2.imread('./img_test1.jpg')
plt.figure()
plt.imshow(plancton)
image(plancton)

ret1,plancton=cv2.threshold(plancton,80,255,cv2.THRESH_BINARY)
plt.figure()
plt.imshow(plancton)


# In[104]:


diametre(plancton)


# In[ ]:





# In[ ]:




