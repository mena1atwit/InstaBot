import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setFixedWidth(1000)

        mainLayout = QVBoxLayout()
        self.setStyleSheet("""QLineEdit{height: 15px; font-size: 15px}QLabel{font-size: 15px}""")

        #like
        self.max_number_of_likes = QLineEdit()
        self.tags_like = QLineEdit()
        self.delay_like = QLineEdit()
        self.skip_top_nine_like = QLineEdit()
        self.order_like = QLineEdit()

        mainLayout.addWidget(QLabel('like:'))
        mainLayout.addWidget(self.max_number_of_likes)
        mainLayout.addWidget(self.tags_like)
        mainLayout.addWidget(self.delay_like)
        mainLayout.addWidget(self.skip_top_nine_like)
        mainLayout.addWidget(self.order_like)

        #comment
        self.max_number_of_comments = QLineEdit()
        self.tags_comment = QLineEdit()
        self.delay_comment = QLineEdit()
        self.skip_top_nine_like_comment = QLineEdit()
        self.order_like_comment = QLineEdit()
        self.comment_input = QLineEdit()

        mainLayout.addWidget(QLabel('dm:'))
        mainLayout.addWidget(self.max_number_of_comments)
        mainLayout.addWidget(self.tags_comment)
        mainLayout.addWidget(self.delay_comment)
        mainLayout.addWidget(self.skip_top_nine_like_comment)
        mainLayout.addWidget(self.order_like_comment)
        mainLayout.addWidget(self.comment_input)


        #dm
        self.max_number_of_dms = QLineEdit()
        self.dm_input = QLineEdit()
        self.skip_top_nine_dm = QLineEdit()
        self.tags_dm = QLineEdit()
        self.users_dm = QLineEdit()
        self.delay_dm = QLineEdit()

        mainLayout.addWidget(QLabel('dm:'))
        mainLayout.addWidget(self.max_number_of_dms)
        mainLayout.addWidget(self.dm_input)
        mainLayout.addWidget(self.skip_top_nine_dm)
        mainLayout.addWidget(self.tags_dm)
        mainLayout.addWidget(self.users_dm)
        mainLayout.addWidget(self.delay_dm)


        #follow
        self.accounts_to_follow = QLineEdit()
        self.follow_followers = QLineEdit()
        self.follow_likers = QLineEdit()
        self.post_index = QLineEdit()
        self.tags_follow = QLineEdit()
        self.delay_follow = QLineEdit()
        self.skip_top_nine_follow = QLineEdit()

        mainLayout.addWidget(QLabel('dm:'))
        mainLayout.addWidget(self.accounts_to_follow)
        mainLayout.addWidget(self.follow_followers)
        mainLayout.addWidget(self.follow_likers)
        mainLayout.addWidget(self.post_index)
        mainLayout.addWidget(self.tags_follow)
        mainLayout.addWidget(self.delay_follow)
        mainLayout.addWidget(self.skip_top_nine_follow)


        #unfollow
        self.users_unfollow = QLineEdit()
        self.whitelist = QLineEdit()
        self.desired_unfollowing = QLineEdit()
        self.delay_unfollow = QLineEdit()

        mainLayout.addWidget(QLabel('dm:'))
        mainLayout.addWidget(self.users_unfollow)
        mainLayout.addWidget(self.whitelist)
        mainLayout.addWidget(self.desired_unfollowing)
        mainLayout.addWidget(self.delay_unfollow)


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