import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
import matplotlib.pyplot as plt
import cv2

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras import layers
import pandas as pd
from tensorflow.keras.applications import DenseNet121

cwd = os.getcwd()

model = keras.models.load_model(f'{cwd}\DN121v3')
print(model.summary())

def predict():
    dir_path = f'./../data/test'
    correct =0
    incorrect =0
    total =0

    TruePositive=0   #ทายว่า correct ออกมาเป็น corect
    TrueNegative=0  #ทายว่า incorrect ออมาเป็น incorect
    FalsePositive=0  #ทายว่า correct แต่ออกมาเป็น incorrect
    FalseNegative=0  #ทายว่า incorrect แต่ออกมาเป็น correct

    for i in os.listdir(dir_path):
        img = tf.keras.preprocessing.image.load_img(dir_path+'//'+i, target_size=(224,224))
        

        X= tf.keras.preprocessing.image.img_to_array(img)
        X= np.expand_dims(X,axis=0)
        image = np.vstack([X])
        val = model.predict(image)

        #correct > incorrect
        if float(val[0][0]) > float(val[0][1]):
            total +=1
            if 'cor' in i:
                correct +=1
                TruePositive +=1
            else:
                incorrect +=1
                FalsePositive +=1
            print('model prediction : correct')

        #incorrect > correct
        elif float(val[0][0]) < float(val[0][1]):
            total +=1
            if 'in' in i:
             correct +=1
             TrueNegative +=1
            else:
             incorrect +=1
             FalseNegative +=1
            print('model prediction : incorrect')  

        
        # print(float(val[0][0]))
        # print(float(val[0][1]))
        print(val,i)
        print('============================================')  
    print('actual           : ', total)
    print('actual correct   : ', correct)
    print('actual incorrect : ', incorrect)
    print('correct          : {:.2%}'.format(correct/total))
    print('incorrect        : {:.2%}'.format(incorrect/total))
    print('============================================')  
    print('true positive    : ', TruePositive)
    print('true negative    : ', TrueNegative)
    print('false positive   : ', FalsePositive)
    print('false negative   : ', FalseNegative)    

predict()

# dir_path = './../data/test'

# for i in os.listdir(dir_path):
#     print(i)