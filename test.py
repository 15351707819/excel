# from PyQt5.QtCore import QObject, pyqtSignal
#
#
# class QTypeSignal(QObject):
#     sendmsg = pyqtSignal(str, str)
#
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         self.sendmsg.emit('第一个参数', '第二个参数')
#
#
# class QTypeSlot(QObject):
#     def __int__(self):
#         super().__int__()
#
#     def get(self, msg1, msg2):
#         print("QSlot get msg =>" + msg1 + '' + msg2)
#
#
# if __name__ == '__main__':
#     print("===connect===")
#     send = QTypeSignal()
#     slot = QTypeSlot()
#     send.sendmsg.connect(slot.get)
#     send.run()
#     print("===disconnect===")
#     send.sendmsg.disconnect(slot.get)
#     send.run()
