from ImageModules import detectFace
from ImageModules import noiseReduction
'''
Main class for facedetection, where it has instances of all the class, file handling and choice option.
'''
class FaceDetectionMain:
	def main():
		#creating an empty list
		imageList = []
		choice = True
		#opening a text to access the list of image paths
		try:
			while choice == True:
				imageChoice = raw_input("Enter the kind the image you want for face detection : group or single?")
				if imageChoice == "single":
					imageFile = open('singleImage_location.txt')
					choice = False
				elif imageChoice == "group":
					imageFile = open('GroupImage_location.txt')
					choice = False
				else:
					print "Enter a valid choice"

		except Exception as e:
			print "Error : Unable to open file"
		else:
			#reading image papths from a file to a list using list comprehension
			imageList = [line.strip() for line in imageFile.readlines()]
			imageFile.close()

			#creating an object for class detectFace
			faceDetectionObj = detectFace.FaceDetect(imageList,imageChoice)

			#accessing the the method in class detectFace 
			faceDetectionObj.imgRead()

			imagesmoothObj = noiseReduction.ImageSmooth(imageList,imageChoice)
			imagesmoothObj.imageSmooth()

			

	#This is run first when we execute the python file.
	if __name__ == '__main__':
			main()