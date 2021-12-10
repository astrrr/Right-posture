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
from main import MainWindow
from plyer import notification
from pypresence import Presence
import time
# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):

    # Notification function
    def notifyMe(self, title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=10,
            app_icon="bin/Icon/iconTimer.ico"
        )
        self.ui.Detail_text.append("Print notification")

    # Discord Rich Presence
    def discordRichPresence(self):
        if self:
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
                print("Discord Rich Presence Connected")
            except:
                print("Pipe Not Found - Is Discord Running?")