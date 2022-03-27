from main import MainWindow
from modules import Camera_detail, save_data

class Main_checkbox(MainWindow):
    camera_status = ""
    def Show_Detail(self):
        if self.ui.show_detail.isChecked():
            self.ui.Detail_text.setText(f"Camera VideoCapture(0): {Main_checkbox.camera_status}\n\n"
                                        f"Models: {Camera_detail.get_model_name}\n"
                                        f"Models Status: {Camera_detail.model_status}\n\n"
                                        f"Notification setup\n"
                                        f"Period = {self.ui.combo_period.currentText()}\n"
                                        f"Sensitive = {self.ui.combo_sensitive.currentText()}\n"
                                        f"Sitting = {self.ui.combo_sitting.currentText()}\n"
                                        f"{Camera_detail.traceback}")
            save_data("PreDetail", 1)
            # print("Start Detail")
        else:
            self.ui.Detail_text.clear()
            save_data("PreDetail", 0)
            # print("Stop Detail")

    def Detect_Log(self):
        self.ui.Detect_LOG.append(Camera_detail.log)
        Camera_detail.Update_log = False
        # print("Print Log")