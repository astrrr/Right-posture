from main import MainWindow
from PySide6 import QtWidgets
import sqlite3

class Main_table(MainWindow):

    def load_test(self, user_setting):
        conn = sqlite3.connect('sessions.db')
        cur = conn.cursor()
        query = f"SELECT * " \
                f"FROM sessions WHERE user_id = \'{user_setting}\'"
        cur.execute(query)
        try:
            results = cur.fetchall()
            table_row = 0
            self.ui.Status_Widgets_2.setRowCount(len(results))
            for row in results:
                self.ui.Status_Widgets_2.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.Status_Widgets_2.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.Status_Widgets_2.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
                table_row += 1

            print(results)
        except Exception as e:
            print(e)

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