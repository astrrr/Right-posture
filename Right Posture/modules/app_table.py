from main import MainWindow
from PySide6 import QtWidgets
import sqlite3

class Main_table(MainWindow):

    def Load_table(self, user_id):
        conn = sqlite3.connect('sessions.db')
        cur = conn.cursor()
        query = f"SELECT user_id, time_start, time_end, incorrect_time, correct_time, total_time, incorrect_per,correct_per " \
                f"FROM sessions WHERE user_id = \'{user_id}\'"
        cur.execute(query)
        try:
            results = cur.fetchall()
            self.ui.Log_table.setRowCount(0)
            for row_number, row_data in enumerate(results):
                self.ui.Log_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number < 6:
                        self.ui.Log_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        self.ui.Log_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)+' %'))
            print("loaded")
        except Exception as e:
            print(e)