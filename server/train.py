import os
import cv2
import numpy as np
import squares
import processImage as pImg 

# ============================================================================    

def output_chars(chars, labels):
    for i, char in enumerate(chars):
        filename = "chars/%s.png" % labels[i]
        char = cv2.resize(char
            , None
            , fx=3
            , fy=3
            , interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(filename, char)

# ============================================================================    
def train(plateNo):
    try:
        plate_chars=[]
        if not os.path.exists("chars"):
            os.makedirs("chars")
        #plateNo=raw_input('\nEnter Plate Number:')
        plateList=list(plateNo)
        # img_plate = cv2.imread('lplate2.png')
        img_plate=squares.getPlateRegion()
        img = pImg.clean_image(img_plate)
        clean_img, plateNoImages = pImg.extract_characters(img)
        output_img = pImg.highlight_characters(clean_img, plateNoImages)
        cv2.imwrite('licence_plate_out.png', output_img)
        for bbox,char_imgs in plateNoImages:
            plate_chars.append(char_imgs)
        if len(plate_chars)!=len(plateList):
            raise ValueError("didnt detect all chars")
        output_chars(plate_chars, plateList)
        setPlates=set(plateList)
        genData(setPlates)
        print "sucessfully trained"
        return 
    except:
        print "training unsucessful"

# ============================================================================ 
def load_char_images(CHARS):
    characters = {}
    for char in CHARS:
        char_img = cv2.imread("chars/%s.png" % char, 0)
        characters[char] = char_img
    return characters

# ============================================================================
def genData(CHARS):
    characters = load_char_images(CHARS)

    samples =  np.empty((0,100))
    for char in CHARS:
        char_img = characters[char]
        small_char = cv2.resize(char_img,(10,10))
        sample = small_char.reshape((1,100))
        samples = np.append(samples,sample,0)

    responses = np.array([ord(c) for c in CHARS],np.float32)
    responses = responses.reshape((responses.size,1))
    samples_h=file('char_samples.data','a')
    responses_h=file('char_responses.data','a')
    np.savetxt(samples_h,samples)
    np.savetxt(responses_h,responses)

if __name__ == "__main__":
    train()
