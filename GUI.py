import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setFixedWidth(800)

        mainLayout = QVBoxLayout()
        self.setStyleSheet("""
            QLineEdit{height: 40px; font-size: 30px}
            QLabel{font-size: 30px}
        """)

        self.name = QLineEdit()
        self.age = QLineEdit()
        mainLayout.addWidget(QLabel('weweee:'))
        mainLayout.addWidget(self.name)
        mainLayout.addWidget(QLabel('yyeee:'))
        mainLayout.addWidget(self.age)

        self.Confirm = QPushButton('Confirm')
        self.Confirm.setStyleSheet('font-size: 30px')
        # self.Confirm.clicked.connect(self.passingInformation)
        mainLayout.addWidget(self.Confirm)

        self.setLayout(mainLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())