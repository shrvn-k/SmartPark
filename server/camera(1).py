import cv2
import picamera
def getImage():
	try:
		camera=picamera.PiCamera()
		camera.capture('lp1.jpg')
		camera.close()
		return cv2.imread('lp1.jpg')
	except:
		return 

if __name__ == "__main__":
    getImage()
