from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal, Slot, QThread

import sys
import cv2
import numpy as np
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
class VideoThread(QThread):
   # シグナル設定
   change_pixmap_signal = Signal(np.ndarray)

   def __init__(self):
       super().__init__()
       self._run_flag = True

   # QThreadのrunメソッドを定義
   def run(self):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:
        while self._run_flag:
            success, image = cap.read()
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)

            # Draw landmark annotation on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image,
                results.face_landmarks,
                mp_holistic.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_contours_style())
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles
                .get_default_pose_landmarks_style())
           # 新たなフレームを取得できたら
           # シグナル発信(cv_imgオブジェクトを発信)            
            if success:
               self.change_pixmap_signal.emit(image)
        cap.release()
        cv2.destroyAllWindows()
       # videoCaptureのリリース処理
        
   # スレッドが終了するまでwaitをかける
   def stop(self):
       self._run_flag = False
       self.wait()

class Start_Camera:
   def detect(self):
       self.image_label = QLabel(self)

       # vboxにQLabelをセット
       vbox = self.ui.gridLayout_2
       vbox.addWidget(self.image_label)

       # vboxをレイアウトとして配置
       self.setLayout(vbox)

       # ビデオキャプチャ用のスレッドオブジェクトを生成
       self.thread = VideoThread()
       # ビデオスレッド内のchange_pixmap_signalオブジェクトのシグナルに対するslot
       self.thread.change_pixmap_signal.connect(self.update_image)

       self.thread.start() # スレッドを起動