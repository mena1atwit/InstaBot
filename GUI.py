from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("InstaBot")
        self.initGUI()

    def initGUI(self):
        self.like_btn = QtWidgets.QPushButton(self)
        self.like_btn.setText("Like")
        self.comment_btn = QtWidgets.QPushButton(self)
        self.comment_btn.setText("Comment")
        self.follow_btn = QtWidgets.QPushButton(self)
        self.follow_btn.setText("Follow")
        self.unfollow_btn = QtWidgets.QPushButton(self)
        self.unfollow_btn.setText("Unfollow")

        #self.vbox = QtWidgets.QVBoxLayout(self)



def gui():
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec_())

gui()
