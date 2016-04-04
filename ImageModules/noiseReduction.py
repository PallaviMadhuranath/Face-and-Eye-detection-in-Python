import cv2
import numpy as np

'''
This class makes the image smooth by reducing the noise in an image using Non local means denoising.

'''

class ImageSmooth():
  def __init__(self,imageList,choice):
    self.imageList = imageList
    self.choice = choice

  def imageSmooth(self):
    if self.choice == "single":
      for i in self.imageList:
        self.image = cv2.imread(i)
        self.newx,self.newy = self.image.shape[1]/2,self.image.shape[0]
        self.newimage = cv2.resize(self.image,(self.newx,self.newy))
        self.dst = cv2.fastNlMeansDenoisingColored(self.newimage,None,5,5,7,21) 
        self.vis = np.concatenate((self.newimage, self.dst), axis=1)
        self.imageShow()

  def imageShow(self):
    cv2.imshow('blur',self.vis)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#from matplotlib import pyplot as plt
#img = cv2.imread('/Users/pallavidas/Dropbox/Courses/Quarter2/python/Image_Processing/Image/w.jpg')
