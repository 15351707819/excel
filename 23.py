
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QToolBar
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建帮助按钮
        help_action = QAction(QIcon('help_icon.png'), 'Help', self)
        help_action.setShortcut('Ctrl+H')
        help_action.triggered.connect(self.show_help)

        # 创建帮助菜单
        help_menu = QMenu(self)
        help_menu.addAction(help_action)

        # 创建菜单栏并添加菜单
        menu_bar = self.menuBar()
        menu_bar.addMenu(help_menu)

        # 创建工具栏并添加按钮
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)
        toolbar.addAction(help_action)

        self.setWindowTitle('Help Button Example')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def show_help(self):
        # 处理帮助操作的逻辑
        print('Help action triggered')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()