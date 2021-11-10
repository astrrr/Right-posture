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
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# GUI FILE
from . ui_main import Ui_MainWindow

# Login FILE
from . ui_login import Ui_Login

# APP SETTINGS
from . app_settings import *

# IMPORT MAIN FUNCTIONS
from . ui_main_functions import *

# IMPORT LOGIN FUNCTIONS
from . ui_login_function import *

# APP FUNCTIONS
from . app_functions import *

# DETECT FUNCTIONS
from . app_detect import Start_Camera

# APP DATA
from . app_data import *