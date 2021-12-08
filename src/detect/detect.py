import cv2
import mediapipe as mp
import os
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.models import Model
import numpy as np

cwd = os.getcwd()

def predict(img):
  img = tf.keras.preprocessing.image.load_img(cwd+'//'+img, target_size=(224,224))
  # img = tf.keras.preprocessing.image.load_img(img, target_size=(224,224))
  
  #resized = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)
  X= tf.keras.preprocessing.image.img_to_array(img)
  
  # X= tf.keras.preprocessing.image.img_to_array(resized)
  X= np.expand_dims(X,axis=0)
  image = np.vstack([X])
  val = model.predict(image)
  
  #correct > incorrect
  if float(val[0][0]) > float(val[0][1]):
    print('model prediction : correct')
    return 0  
  #incorrect > correct
  elif float(val[0][0]) < float(val[0][1]):
    print('model prediction : incorrect')
    return 1

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose





# For webcam input:



#load model
model = tf.keras.models.load_model(f'{cwd}\..\DN121v3')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
pred = 3
img_counter_cor = 0
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # image = cv2.resize(image, (224, 224), interpolation = cv2.INTER_AREA)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    
    if pred == 0:
      cv2.putText(image, "Correct", (20, 20), 2, 0.5, (0, 255, 0), 1)
          
    if pred == 1:
      cv2.putText(image, "Incorrect", (20, 20), 2, 0.5, (0, 0, 255), 1)  
    
    
    # print('==============================')
    # predict(image)


    # Flip the image horizontally for a selfie-view display.
    #cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
    cv2.imshow('MediaPipe Pose', image)
    

    
    #capture pic ture for data set
    img_name = "temp_{}.png".format(img_counter_cor)
    cv2.imwrite(img_name, image)
    print("{} written!".format(img_name))
    img_counter_cor += 1
    
    predict
    for i in os.listdir(cwd):
      if '.png' in i:
        print('=======================')
        pred = predict(i)
        
        
    #     print(pred)
        os.remove(i)
    
    
    
    #press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
      break
      
      
    

cap.release()