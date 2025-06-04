import sys

import datetime
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QVBoxLayout, QApplication, QMessageBox, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from windowpage import Ui_MainWindow
from helpdiaglog import Ui_Dialog
from version import Ui_Dialog as Version_Ui
import dealFile
import function

# 版本生成日期
APP_VERSION = "1.0.0"
BUILD_DATE = datetime.datetime.now().strftime("%Y-%m-%d")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.input_path = None
        self.brand = '10'            # brand值为10时----信捷，高电平为0；brand为01时----四川零点
        self.logic = 'k'
        self.channel = 1
        self.DataFrame = None
        self.flag = 0
        self.setupUi(self)

        self.sichuan.setProperty('brand', '01')
        self.xinje.setProperty('brand', '10')
        self.KVIS.setProperty('logic', 'k')
        self.ZD.setProperty('logic', 'z')
        self.tongdao1.setProperty('channel', 1)
        self.tongdao2.setProperty('channel', 2)

        self.sichuan.clicked.connect(self.GetBrand)
        self.xinje.clicked.connect(self.GetBrand)
        self.KVIS.clicked.connect(self.GetLogic)
        self.ZD.clicked.connect(self.GetLogic)
        self.tongdao1.clicked.connect(self.GetChannel)
        self.tongdao2.clicked.connect(self.GetChannel)

        self.pushButton.clicked.connect(self.upload)
        self.pushButton_2.clicked.connect(self.DrawFigure)
        self.pushButton_3.clicked.connect(self.DrawBar)

        self.max.clicked.connect(self.ReceiveMax)
        self.min.clicked.connect(self.ReceiveMin)
        self.average.clicked.connect(self.AverageValue)
        self.count.clicked.connect(self.ReceiveCounts)

        self.actionhelp.triggered.connect(self.HelpNews)
        self.version.triggered.connect(self.VersionINFO)

    def upload(self):
        wordfile, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "/", "Excel文件(*.xlsx;*.csv)")
        fileinfo = QFileInfo(wordfile)
        filePath = fileinfo.absoluteFilePath()
        self.label.setText(filePath)
        self.input_path = str(self.label.text())
        if self.input_path is None or self.input_path == '':
            self.flag = 0
        else:
            self.flag = 1
            self.DataFrame = dealFile.column_data(
                inputpath=self.input_path,
                channel=self.channel,
                logic=self.logic,
                brand=self.brand)

    def GetBrand(self):
        sender = self.sender()
        new_brand = sender.property('brand')
        self.brand = new_brand

    def GetLogic(self):
        sender = self.sender()
        self.logic = sender.property('logic')

    def GetChannel(self):
        sender = self.sender()
        self.channel = sender.property('channel')

    def DrawFigure(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                self, "error", "文件路径不存在,请选择文件")
        elif self.flag == 1:
            function.DrawPlot(self.DataFrame)

    def DrawBar(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                self, "error", "文件路径不存在，请选择文件")
        elif self.flag == 1:
            function.DrawBargraph(self.DataFrame)

    def ReceiveMax(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                self, "error", "文件路径不存在，请选择文件")
        elif self.flag == 1:
            self.maxvalue.setText(str(function.GetMax(self.DataFrame)))

    def ReceiveMin(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                self, "error", "文件路径不存在，请选择文件"
            )
        elif self.flag == 1:
            self.minvalue.setText(str(function.GetMin(self.DataFrame)))

    def AverageValue(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                self, "error", "文件路径不存在，请选择文件"
            )
        elif self.flag == 1:
            self.avervalue.setText(str(function.GetAverage(self.DataFrame)))

    def ReceiveCounts(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                self, "error", "文件路径不存在，请选择文件"
            )
        elif self.flag == 1:
            self.countsvalue.setText(str(function.GetCounts(self.DataFrame)))

    def HelpNews(self):
        helpMessage = HelpDialog()
        helpMessage.exec_()

    def VersionINFO(self):
        versionmessage = VersionDialog()
        versionmessage.softversion.setText(APP_VERSION)
        versionmessage.builddate.setText(BUILD_DATE)
        versionmessage.exec_()


class HelpDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class VersionDialog(QDialog, Version_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
