import sys


from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QVBoxLayout, QApplication, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from windowpage import Ui_MainWindow
from helpdiaglog import Ui_Dialog
import parse


class PlotWindow(QDialog):
    def __init__(self, figure):
        super().__init__()
        self.figure = figure
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.figure = None
        self.input_path = None
        self.brand = '10'
        self.flag = 0
        self.setupUi(self)
        self.pushButton.clicked.connect(self.upload)
        self.pushButton_2.clicked.connect(self.DrawFigure)
        self.min.clicked.connect(self.GetMin)
        self.max.clicked.connect(self.GetMax)
        self.average.clicked.connect(self.GetAvg)
        self.average_2.clicked.connect(self.GetCount)
        self.pushButton_3.clicked.connect(self.DrawBBB)
        self.actionhelp.triggered.connect(self.HelpMessage)
        self.xinje.clicked.connect(self.GetXinje)
        self.sichuan.clicked.connect(self.Getsichuan)

    def upload(self):
        wordfile, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "/", "Excel 文件(*.xlsx;*.csv)")
        fileinfo = QFileInfo(wordfile)
        filename = fileinfo.fileName()
        filePath = fileinfo.absoluteFilePath()
        self.label.setText(filePath)
        self.input_path = str(self.label.text())
        if self.input_path is None:
            self.flag = 0
        else:
            self.flag = 1

    def DrawFigure(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                window.centralWidget(), "error", "文件路径不存在,请选择文件")
        elif self.flag == 1:
            self.figure = parse.DrawPlot(self.input_path, self.brand)
            plot_window = PlotWindow(self.figure)
            plot_window.exec_()

    def DrawBBB(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                window.centralWidget(), "error", "文件路径不存在,请选择文件")
        elif self.flag == 1:
            parse.DrawBar(self.input_path, self.brand)

    def GetMax(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                window.centralWidget(), "error", "文件路径不存在,请选择文件")
        elif self.flag == 1:
            maxvalue1 = parse.GetMaxValue(self.input_path, self.brand)
            self.maxvalue.setText(str(maxvalue1))

    def GetMin(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                window.centralWidget(), "error", "文件路径不存在,请选择文件")
        elif self.flag == 1:
            minvalue1 = parse.GetMinValue(self.input_path, self.brand)
            self.minvalue.setText(str(minvalue1))

    def GetAvg(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                window.centralWidget(), "error", "文件路径不存在,,请选择文件")
        elif self.flag == 1:
            avervalue1 = parse.GetAverageValue(self.input_path, self.brand)
            self.avervalue.setText(str(avervalue1))

    def GetCount(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                window.centralWidget(), "error", "文件路径不存在,请选择文件")
        elif self.flag == 1:
            counts = parse.GetCounts(self.input_path, self.brand)
            self.countsvalue.setText(str(counts))

    def HelpMessage(self):
        helpmessage = HelpDiaglog()
        helpmessage.exec_()

    def GetXinje(self):
        self.brand = '10'

    def Getsichuan(self):
        self.brand = '01'


class HelpDiaglog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
