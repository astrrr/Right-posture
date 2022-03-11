from PySide6 import QtCore, QtGui, QtWidgets, QtCharts
import sys

def chart(self):

    data = {
        "Correct 70%": (70, QtGui.QColor("#bd93f9")),
        "Incorrect 30%": (30, QtGui.QColor("#ff79c6")),
    }

    series = QtCharts.QPieSeries()
    series.setHoleSize(0.4)
    for name, (value, color) in data.items():
        _slice = series.append(name, value)
        _slice.setBrush(color)

    chart = QtCharts.QChart()
    chart.addSeries(series)
    chart.setTitle("Example for https://stackoverflow.com/questions/5672a7499")
    chart.legend().setAlignment(QtCore.Qt.AlignBottom)
    chart.legend().setFont(QtGui.QFont("Arial", 20))

    chartview = QtCharts.QChartView(chart)
    chartview.setRenderHint(QtGui.QPainter.Antialiasing)
