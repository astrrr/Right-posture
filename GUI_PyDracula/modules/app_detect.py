from main import *
import cv2
import mediapipe as mp
import tensorflow as tf
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cwd = os.getcwd()
model = None
first_load = True

class VideoThread(QThread):
    # シグナル設定
    change_pixmap_signal = Signal(np.ndarray)
    def __init__(self):
        super().__init__()
        self._run_flag = True
        global model
        global first_load
        if first_load:
            print("Start Load model")
            modeling = tf.keras.models.load_model(f'{cwd}\DN121v3')
            print("Finish load model")
            model = modeling
            first_load = False
    # QThreadのrunメソッドを定義
    def run(self):
        # load model
        count_log = 0
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        pred = 3
        img_counter_cor = 0
        with mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as pose:
            while self._run_flag:
                success, raw = cap.read()
                resize = cv2.resize(raw, (384, 288))
                image = cv2.flip(resize, 1)

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

                # capture pic ture for data set
                img_name = "temp_{}.png".format(img_counter_cor)
                cv2.imwrite(img_name, image)
                # ///////////////////////////////////////////////////////////////////////////////
                Camera.log = ("{} written!".format(img_name))
                print("{} written!".format(img_name))
                # ///////////////////////////////////////////////////////////////////////////////
                img_counter_cor += 1

                self.predict
                for i in os.listdir(cwd):
                    if '.png' in i:
                        # ///////////////////////////////////////////////////////////////////////////////
                        Camera.log = (Camera.log + '\n=======================')
                        print('=======================')
                        # ///////////////////////////////////////////////////////////////////////////////
                        pred = self.predict(i)
                        #     print(pred)
                        os.remove(i)

                # 新たなフレームを取得できたら
                # シグナル発信(cv_imgオブジェクトを発信)
                if success:
                    self.change_pixmap_signal.emit(image)
            cap.release()
            cv2.destroyAllWindows()
        # videoCaptureのリリース処理

    def predict(self, img):
        img = tf.keras.preprocessing.image.load_img(cwd + '//' + img, target_size=(224, 224))
        # img = tf.keras.preprocessing.image.load_img(img, target_size=(224,224))

        # resized = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)
        X = tf.keras.preprocessing.image.img_to_array(img)

        # X= tf.keras.preprocessing.image.img_to_array(resized)
        X = np.expand_dims(X, axis=0)
        image = np.vstack([X])
        val = model.predict(image)

        # correct > incorrect
        if float(val[0][0]) > float(val[0][1]):
            # ///////////////////////////////////////////////////////////////////////////////
            Camera.log = (Camera.log + '\nmodel prediction : correct')
            print('model prediction : correct')
            # ///////////////////////////////////////////////////////////////////////////////
            return 0
            # incorrect > correct
        elif float(val[0][0]) < float(val[0][1]):
            # ///////////////////////////////////////////////////////////////////////////////
            Camera.log = (Camera.log + '\nmodel prediction : incorrect')
            print('model prediction : incorrect')
            # ///////////////////////////////////////////////////////////////////////////////
            return 1

    # スレッドが終了するまでwaitをかける
    def stop(self):
        self._run_flag = False
        self.wait()

class Camera:
    log = ""
    def detect(self, enable):
        if enable:
            self.image_label = QLabel(self)

            # vboxにQLabelをセット
            Camera_1 = self.ui.Camera_Frame_1_Layout
            Camera_1.addWidget(self.image_label)

            # vboxをレイアウトとして配置
            self.setLayout(Camera_1)

            # ビデオキャプチャ用のスレッドオブジェクトを生成
            self.thread = VideoThread()
            # ビデオスレッド内のchange_pixmap_signalオブジェクトのシグナルに対するslot
            self.thread.change_pixmap_signal.connect(self.update_image)

            self.thread.start()  # スレッドを起動
        else:
            try:
                self.ui.Camera_Frame_1_Layout.removeWidget(self.image_label)
                self.image_label.deleteLater()
                self.thread.stop()
            except:
                pass