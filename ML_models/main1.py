# import tensorflow_datasets as tfds
import tensorflow as tf
# import the necessary packages
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2,InceptionV3,VGG16,MobileNetV3Large
from tensorflow.keras.layers import AveragePooling2D,Dropout,Convolution2D,MaxPooling2D
from tensorflow.keras.layers import Dropout,BatchNormalization,Conv2D
from tensorflow.keras.layers import Flatten,Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam,SGD
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import to_categorical
# from sklearn.preprocessing import LabelBinarizer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report
# from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os
import keras
# from tensorflow.keras.datasets import fashion_mnist
import cv2
# from google.colab.patches import cv2_imshow
import tarfile
import pandas as pd


label_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

BS = 16
model = tf.keras.models.load_model('.\ML_models\FASHION-MNNIST-SGD.model')
# model = tf.keras.models.load_model('.\FASHION-MNNIST-SGD.model')
def predimage(link,y):
    from PIL import Image,ImageDraw
    # link="./media/images/shoe1.jpg"
    image = Image.open(link)
    test = cv2.imread(link,cv2.IMREAD_GRAYSCALE)
    test = cv2.resize(test, (28, 28))
    test = 255 - test
    test = img_to_array(test)
    test = np.expand_dims(test,axis=0)
    #test /= 255 
    result = model.predict(test,batch_size = BS)
    y_class = result.argmax(axis=1)
    result = (result*100)
    result = list(np.around(np.array(result),1))
    i = y_class[0]
    s = result[0][i]
    plt.text(1, 1,y[i],size=30,color='red', horizontalalignment='left',verticalalignment='top')
    plt.text(0.5, 0.5,s,size=25,color='green',horizontalalignment='right',verticalalignment='bottom')
    plt.imshow(image)
    print(result)
    print(y[i])
    return(y[i])

# predimage('./shoe1.jpg',label_names)