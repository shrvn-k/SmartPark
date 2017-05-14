import cv2
import numpy as np

def reduce_colors(img, n):
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = n
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    return res2 

# ============================================================================

def clean_image(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    resized_img = cv2.resize(gray_img
        , None
        , fx=5.0
        , fy=5.0
        , interpolation=cv2.INTER_CUBIC)

    resized_img = cv2.GaussianBlur(resized_img,(5,5),0)
    cv2.imwrite('licence_plate_large.png', resized_img)

    equalized_img = cv2.equalizeHist(resized_img)
    cv2.imwrite('licence_plate_equ.png', equalized_img)


    reduced = cv2.cvtColor(reduce_colors(cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGR), 8), cv2.COLOR_BGR2GRAY)
    cv2.imwrite('licence_plate_red.png', reduced)


    ret, mask = cv2.threshold(reduced, 70, 255, cv2.THRESH_BINARY)
    #ret, mask = cv2.threshold(reduced, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite('licence_plate_mask.png', mask) 

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    #mask = cv2.erode(mask, kernel, iterations = 1)
    cv2.imwrite('licence_plate_mask2.png', mask)

    return mask

# ============================================================================

def extract_characters(img):
    bw_image = cv2.bitwise_not(img)
    contours = cv2.findContours(bw_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

    char_mask = np.zeros_like(img)
    bounding_boxes = []
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        #print "\n",w,"---",h
        area = w * h
        center = (x + w/2, y + h/2)
        if  (w>35) and (h>90) and (w<80) and (h<140):
            
            x,y,w,h = x-4, y-4, w+8, h+8
            bounding_boxes.append((center, (x,y,w,h)))
            cv2.rectangle(char_mask,(x,y),(x+w,y+h),255,-1)

    cv2.imwrite('licence_plate_mask3.png', char_mask)

    clean = cv2.bitwise_not(cv2.bitwise_and(char_mask, char_mask, mask = bw_image))

    bounding_boxes = sorted(bounding_boxes, key=lambda item: item[0][0])  

    characters = []
    for center, bbox in bounding_boxes:
        x,y,w,h = bbox
        char_image = clean[y:y+h,x:x+w]
        characters.append((bbox,char_image))
    return clean, characters

def highlight_characters(img, chars):
    output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for bbox, char_img in chars:
        x,y,w,h = bbox
        cv2.rectangle(output_img,(x,y),(x+w,y+h),255,1)

    return output_img
