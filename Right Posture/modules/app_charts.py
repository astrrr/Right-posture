from PySide6.QtWidgets import QVBoxLayout, QWidget
import pandas as pd
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

class Line_charts(QWidget):
    def __init__(self, result_des, result_fet):
        super().__init__()
        self.setWindowTitle('Latest use')
        self.init_ui(result_des, result_fet)

    def init_ui(self, results_description, results_fetch):
        cols = [column[0] for column in results_description]
        results = pd.DataFrame.from_records(data=results_fetch, columns=cols)
        # print(results)

        # _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_
        # Line chart
        fig = plt.figure(dpi=100)
        ax = fig.add_subplot(111, title=self.windowTitle())
        plt.subplots_adjust(bottom=0.2, left=0.2, right=0.8, top=0.9)
        ax.grid(True)

        # Create x index
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