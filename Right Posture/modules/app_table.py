from main import MainWindow
from PySide6 import QtWidgets

class Main_table(MainWindow):

    def Load_Table(self):
        people = [{"test": "james", "text": "idk", "cell": "eiei", "Line": "las"},
                  {"test": "eak", "text": "idk", "cell": "eiei", "Line": "las"},
                  {"test": "sun", "text": "idk", "cell": "eiei", "Line": "las"},
                  {"test": "cry", "text": "idk", "cell": "eiei", "Line": "las"},
                  {"test": "a", "text": "idk", "cell": "eiei", "Line": "las"},
                  {"test": "lot", "text": "idk", "cell": "eiei", "Line": "las"}]
        table_row = 0
        self.ui.Status_Widgets.setRowCount(len(people))
        for row in people:
            self.ui.Status_Widgets.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row["test"]))
            table_row += 1