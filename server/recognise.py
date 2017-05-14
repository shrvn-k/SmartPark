import cv2
import numpy as np
import processImage as pImg 
import squares


# ============================================================================    
def recognise():	
	try:
	    img = cv2.imread("lplate2.png")
	    img_plate=squares.getPlateRegion()
	    img = pImg.clean_image(img_plate)
	    clean_img, chars = pImg.extract_characters(img)

	    output_img = pImg.highlight_characters(clean_img, chars)
	    cv2.imwrite('licence_plate_out.png', output_img)


	    samples = np.loadtxt('char_samples.data',np.float32)
	    responses = np.loadtxt('char_responses.data',np.float32)
	    responses = responses.reshape((responses.size,1))


	    model = cv2.ml.KNearest_create()
	    model.train(samples, cv2.ml.ROW_SAMPLE, responses)

	    plate_chars = ""
	    for bbox, char_img in chars:
	        small_img = cv2.resize(char_img,(10,10))
	        small_img = small_img.reshape((1,100))
	        small_img = np.float32(small_img)
	        retval, results, neigh_resp, dists = model.findNearest(small_img, k = 1)
	        plate_chars += str(chr((results[0][0])))

	    print("Licence plate: %s" % plate_chars)
	    return plate_chars
	except:
	 	print "Error: could not recognise plate"
	 	return

if __name__ == "__main__":
    recognise()