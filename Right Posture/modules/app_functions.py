# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
import time
import smtplib
import os
import base64
from main import MainWindow, Settings
from plyer import notification
from pypresence import Presence
from random import randint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from modules.app_temp import Debug_path, Setting_func

cwd = os.getcwd()
cwd = cwd+Debug_path.path

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):

    def send_Email(self, text=None, subject='Forget password', from_email='rightposture.kmitl.team@gmail.com', to_emails=None):
        assert isinstance(to_emails, list)
        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject
        txt_part = MIMEText(text, 'plain')
        msg.attach(txt_part)
        msg_str = msg.as_string()

        # login to my smtp server
        username = 'rightposture.kmitl.team@gmail.com'
        with open(f"{cwd}/bin/Data/password.txt", "r") as read_file:
            password = read_file.readline()
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(username, base64.b64decode(password).decode("utf-8"))
        server.sendmail(from_email, to_emails, msg_str)
        server.quit()

    def generate_auth_key(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    # Notification function
    def notifyMe(self, title, message):
        if not Setting_func.DND_apply:
            notification.notify(
                title=title,
                message=message,
                timeout=10,
                app_icon=f"{cwd}/bin/Icon/iconTimer.ico"
            )

    def notifyIncorrect(self, title, message):
        if not Setting_func.DND_apply:
            notification.notify(
                title=title,
                message=message,
                timeout=10,
                app_icon=f"{cwd}/bin/Icon/iconIncorrect.ico"
            )

    # Discord Rich Presence
    def discordRichPresence(self, enable):
        if enable:
            try:
                rpc = Presence("902601121124728884")
                rpc.connect()

                rpc.update(  # details="Make Life Better.",
                    state="Dev GUI",
                    large_image="right_posture",
                    large_text="อยากรู้ล่ะสิ",
                    small_image="verify",
                    small_text="Verify by me",
                    buttons=[{"label": "Github", "url": "https://github.com/ussnllmn"}],
                    party_size=[35, 100],
                    start=time.time()
                )
                self.ui.Setting_log.append("Discord Rich Presence Connected")
                print("Discord Rich Presence Connected")
            except Exception as e:
                self.ui.Setting_log.append("Pipe Not Found - Is Discord Running?")
                print(e)

    # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
    Settings.ENABLE_CUSTOM_TITLE_BAR = True
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """
        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")