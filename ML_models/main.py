import os
import cv2
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import model_from_json
# %matplotlib inline

# ----- LOAD SAVED MODEL -----
json_file = open('model.json', 'r')     
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk.")

import numpy as np
# from keras.preprocessing import image
import keras.utils as image

test_image = image.load_img('./floral.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = loaded_model.predict(test_image)

index = np.where(result[0] == 1)[0][0]
print(index)

l=[ 'OTHER', 'animal', 'cartoon', 'chevron','floral', 'geometry', 'houndstooth', 'ikat', 'letter_numb', 'plain', 'polka dot', 'scales', 'skull', 'squares','stars','stripes','tribal']