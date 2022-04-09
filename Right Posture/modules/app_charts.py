from PySide6.QtWidgets import QVBoxLayout, QWidget
import pandas as pd
import matplotlib
from modules.app_temp import Debug_path, superuser
from modules import app_auth
import sqlite3
import os

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

cwd = os.getcwd()
cwd = cwd+Debug_path.path

class Line_charts(QWidget):
    def __init__(self, result_line):
        super().__init__()
        self.setWindowTitle('Latest use')
        self.init_ui(result_line)

    def init_ui(self, result):
        user = superuser.user
        print('user : ',user)
        conn = sqlite3.connect(f"{cwd}/bin/Data/Sessions.db", check_same_thread=False)
        # print('connect DB')
        query = conn.execute("SELECT * FROM sessions WHERE user_id = ?", (user,))
        cols = [column[0] for column in query.description]
        results = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

        print(results)
        

        # Example dataframe
        #df = pd.DataFrame(sess_items)
        #print(df)
        
       
        # _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_
        # SPC chart
        fig = plt.figure(dpi=100)
        ax = fig.add_subplot(111, title=self.windowTitle())
        plt.subplots_adjust(bottom=0.2, left=0.2, right=0.8, top=0.9)
        ax.grid(True)

        # create x index
        index_result = [i+1 for i in range(len(results['correct_time']))]
       
        # Trend
        ax.plot(index_result, results['correct_time'], marker='o', markersize=3, label='Correct', color='#bd93f9')
        ax.plot(index_result, results['incorrect_time'], marker='o', markersize=3, label='Incorrect', color='#ff79c6')
        plt.xlabel('Session #')
        plt.ylabel('Time(Sec)')
        plt.legend()
        
        fig.canvas.draw()

        
        # _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_
        # Canvas & Toolbar
        canvas = FigureCanvas(fig)
        # toolbar = NavigationToolbar(canvas, self)
        # unwanted_buttons = ['Back', 'Forward']
        # for x in toolbar.actions():
        #     if x.text() in unwanted_buttons:
        #         toolbar.removeAction(x)
        # _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_
        # Layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        # layout.addWidget(toolbar)
        layout.addWidget(canvas)
        conn.commit()
        