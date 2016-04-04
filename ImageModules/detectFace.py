import cv2
import numpy as np
import time

'''
This class detects face/faces for single/group images using Haar Algorithm. 
For single images it performs eye detection which also user HaarAlgorithm. 
Have used a list to store images from which they are read to perform detection operations.
Time taken to detect an image is recorded and stored inside a list. 
'''
class FaceDetect:

	'''
	Initialization method
	'''
	def __init__(self,pathList,choice):
		#path for image list
		self.pathList = pathList
		#cascade for face detection
		self.faceCascades =cv2.CascadeClassifier('/Users/pallavidas/Desktop/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_alt.xml')
		#cascade for eye detection
		self.eye_cascade = cv2.CascadeClassifier('/Users/pallavidas/Desktop/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')
		#choice : group/single image
		self.choice = choice
	'''
	Method for reading an image from the path and converting RGB image to Grayscale and also resizing the image.
	'''
	def imgRead(self):
		self.durationList = []
		for i in self.pathList:
			self.path = i
			image = cv2.imread(self.path)
			try:
				height = np.size(image, 0)
				width = np.size(image, 1)
			except Exception, e:
				print "Error : invalid image path / image name"
			else:
				#Image resize
				if(height > 600) & (width > 850):
					image = cv2.resize(image, (0,0), fx=0.25, fy=0.25) 
				else:
					image = image;
		
				grimageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				self.detect(grimageGray,image)
			finally:
				pass
	'''
	Method for detecting face and drawing a rectangle around it. Also detects eyes.
	'''	
	def detect(self,grimageGray,image):
		print "Detecting face/faces"
		start = time.time()
		detectedFaces = self.faceCascades.detectMultiScale(grimageGray, scaleFactor=1.1, minNeighbors=2,minSize=(30,30))
		print type(detectedFaces)
		print len(detectedFaces)
		end = time.time()
		duration = end - start
		self.durationList.append(duration)
		

		#loop to get detected faces and draw a rectangle on them.
		for (x,y,w,h) in detectedFaces:
			cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0),2)
			roi_gray = grimageGray[y:y+h, x:x+w]
			roi_color = image[y:y+h, x:x+w]

			#only if single image is selected by the user.
			if self.choice == "single":
				detectedEyes = self.eye_cascade.detectMultiScale(roi_gray,1.30)
				print len(detectedEyes)
				for (ex,ey,ew,eh) in detectedEyes:
					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
		print "Time took for face detection ", end - start, "seconds"
		print self.durationList
		self.imgShow(image)

	'''
	Method to display image
	'''
	def imgShow(self,image):
		cv2.imshow('img',image)
		#cv2.imshow('img',image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		




	







