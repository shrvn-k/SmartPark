import cv2
import numpy as np

CHARS = ['K','A','1','9','M','G','5','0','2']

# ============================================================================

def load_char_images():
    characters = {}
    for char in CHARS:
        char_img = cv2.imread("chars/%s.png" % char, 0)
        characters[char] = char_img
    return characters

# ============================================================================

characters = load_char_images()

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

# ============================================================================