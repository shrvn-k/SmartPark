import cv2
import camera 
import math, numpy as np


def getPlateRegion():
	img=camera.getImage()
	#cv2.namedWindow("Original Image",cv2.WINDOW_NORMAL)
	###cv2.imshow("Original Image",img)


	# RGB to Gray scale conversion
	img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	#cv2.namedWindow("Gray Converted Image",cv2.WINDOW_NORMAL)
	#cv2.imshow("Gray Converted Image",img_gray)


	# Noise removal with iterative bilateral filter(removes noise while preserving edges)
	noise_removal = cv2.bilateralFilter(img_gray,9,75,75)
	#cv2.namedWindow("Noise Removed Image",cv2.WINDOW_NORMAL)

	#cv2.imshow("Noise Removed Image",noise_removal)


	# Histogram equalisation for better results
	equal_histogram = cv2.equalizeHist(noise_removal)
	#cv2.namedWindow("After Histogram equalisation",cv2.WINDOW_NORMAL)

	#cv2.imshow("After Histogram equalisation",equal_histogram)

	#Morphological opening with a rectangular structure element
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
	morph_image = cv2.morphologyEx(equal_histogram,cv2.MORPH_OPEN,kernel,iterations=15)
	#cv2.namedWindow("Morphological opening",cv2.WINDOW_NORMAL)

	#cv2.imshow("Morphological opening",morph_image)

	# Image subtraction(Subtracting the Morphed image from the histogram equalised Image)
	sub_morp_image = cv2.subtract(equal_histogram,morph_image)
	#cv2.namedWindow("Subtraction image", cv2.WINDOW_NORMAL)

	#cv2.imshow("Subtraction image", sub_morp_image)

	# Thresholding the image
	#ret,thresh_image = cv2.threshold(sub_morp_image,42,255,cv2.THRESH_BINARY)
	ret,thresh_image = cv2.threshold(sub_morp_image,0,255,cv2.THRESH_OTSU)
	#cv2.namedWindow("Image after Thresholding",cv2.WINDOW_NORMAL)
        cv2.imwrite("threshholdimg.png",thresh_image)
	#cv2.imshow("Image after Thresholding",thresh_image)


	# Applying Canny Edge detection
	canny_image = cv2.Canny(thresh_image,250,255)
	#cv2.namedWindow("Image after applying Canny",cv2.WINDOW_NORMAL)

	#cv2.imshow("Image after applying Canny",canny_image)

	canny_image = cv2.convertScaleAbs(canny_image)

	# dilation to strengthen the edges
	kernel = np.ones((3,3), np.uint8)
	# Creating the kernel for dilation
	dilated_image = cv2.dilate(canny_image,kernel,iterations=1)
	#cv2.namedWindow("Dilation", cv2.WINDOW_NORMAL)

	#cv2.imshow("Dilation", dilated_image)


	# Finding Contours in the image based on edges
	new,contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours= sorted(contours, key = cv2.contourArea, reverse = True)[:10]
	# Sort the contours based on area ,so that the number plate will be in top 10 contours
	screenCnt = None
	# loop over our contours
	for c in contours:
		# approximate the contour
		x,y,w,h = cv2.boundingRect(c)
		print "w-",w,"---","h ",h
		# x,y,w,h = cv2.boundingRect(c)
		# lol= dilated_image[y:y+h,x:x+w]
		# cv2.imshow("c",lol)
		# cv2.waitKey()
		#if  (w>175) and (h>60) and (w<530) and (h<120):
		#	screenCnt=c
		if  (w>175) and (h>60) and (w<530) and (h<120):
                        peri = cv2.arcLength(c, True)
                        approx = cv2.approxPolyDP(c, 0.06 * peri, True)  
                        if len(approx) == 4 :  # Select the contour with 4 corners
                                screenCnt = approx
                                break
	x,y,w,h = cv2.boundingRect(screenCnt)
	lplate_img= img[y:y+h,x:x+w]
	TARGET_PIXEL_AREA = 7000
	ratio = float(lplate_img.shape[1]) / float(lplate_img.shape[0])
	new_h = int(math.sqrt(TARGET_PIXEL_AREA / ratio) + 0.5)
	new_w = int((new_h * ratio) + 0.5)

	res = cv2.resize(lplate_img, (new_w,new_h))
	#res = cv2.resize(lplate_img,(200,40))
	#res=cv2.resize(lplate_img,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)
	cv2.imwrite("lplate.png", res)
	#cv2.waitKey()
	return res

if __name__ == "__main__":
	getPlateRegion()
