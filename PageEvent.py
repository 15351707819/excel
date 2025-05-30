import sys


from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QVBoxLayout, QApplication, QMessageBox, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from windowpage import Ui_MainWindow
from helpdiaglog import Ui_Dialog
import dealFile
import function

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.input_path = None
        self.brand = '10'            # brand值为10时----信捷，高电平为0；brand为01时----四川零点
        self.logic = 'k'
        self.channel = 1
        self.DataFrame = None
        self.flag = 1
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

    def upload(self):
        wordfile, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "/", "Excel文件(*.xlsx;*.csv)")
        fileinfo = QFileInfo(wordfile)
        filePath = fileinfo.absoluteFilePath()
        self.label.setText(filePath)
        self.input_path = str(self.label.text())
        if self.input_path is None:
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
        print(self.brand)

    def GetLogic(self):
        sender = self.sender()
        self.logic = sender.property('logic')
        print(self.logic)

    def GetChannel(self):
        sender = self.sender()
        self.channel = sender.property('channel')
        print(self.channel)

    def DrawFigure(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.information(
                window.centralWidget(), "error", "文件路径不存在,请选择文件")
        elif self.flag == 1:
            function.DrawPlot(self.DataFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
