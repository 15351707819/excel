import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("第二个窗口")
        layout = QVBoxLayout()
        self.label = QLabel("这是第二个窗口")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.button = QPushButton("打开第二个窗口")
        self.button.clicked.connect(self.open_second_window)
        self.setCentralWidget(self.button)

        self.second_window = None  # 创建一个变量存储第二个窗口

    def open_second_window(self):
        if not self.second_window:
            self.second_window = SecondWindow()
            self.second_window.show()
            # 连接第二个窗口的关闭事件
            self.second_window.closeEvent = self.on_second_window_close

    def on_second_window_close(self, event):
        # 当第二个窗口关闭时，清除其引用
        self.second_window = None
        event.accept()  # 接受关闭事件


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())