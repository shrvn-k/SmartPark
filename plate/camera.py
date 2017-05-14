import cv2
#import picamera
def getImage():
	try:
		# camera=picamera.PiCamera()
		# camera.capture('lp1.jpg')
		return cv2.imread('OK.jpg')
	except:
		return 

if __name__ == "__main__":
    getImage()