import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QComboBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('InstaBot')
        self.setFixedWidth(1000)

        mainLayout = QVBoxLayout()
        self.setStyleSheet("""QLineEdit{height: 15px; font-size: 15px}QLabel{font-size: 15px}""")

        #like
        self.max_number_of_likes = QLineEdit()
        self.tags_like = QLineEdit()
        #delay top like float
        self.delay_like = QLineEdit()
        self.skip_top_nine_like = QComboBox()
        self.skip_top_nine_like.addItems(["Yes", "No"])
        #order like is an int
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
        self.skip_top_nine_comment = QComboBox()
        self.skip_top_nine_comment.addItems(["Yes", "No"])
        self.order_like_comment = QLineEdit()
        self.comment_input = QLineEdit()

        mainLayout.addWidget(QLabel('Comment:'))
        mainLayout.addWidget(self.max_number_of_comments)
        mainLayout.addWidget(self.tags_comment)
        mainLayout.addWidget(self.delay_comment)
        mainLayout.addWidget(self.skip_top_nine_comment)
        mainLayout.addWidget(self.order_like_comment)
        mainLayout.addWidget(self.comment_input)


        #dm
        self.max_number_of_dms = QLineEdit()
        self.dm_input = QLineEdit()
        self.skip_top_nine_dm = QComboBox()
        self.skip_top_nine_dm.addItems(["Yes", "No"])
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
        self.skip_top_nine_follow = QComboBox()
        self.skip_top_nine_follow.addItems(["Yes", "No"])

        mainLayout.addWidget(QLabel('Follow:'))
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

        mainLayout.addWidget(QLabel('Unfollow:'))
        mainLayout.addWidget(self.users_unfollow)
        mainLayout.addWidget(self.whitelist)
        mainLayout.addWidget(self.desired_unfollowing)
        mainLayout.addWidget(self.delay_unfollow)


        self.Confirm = QPushButton('Confirm')
        self.Confirm.setStyleSheet('font-size: 30px')
        mainLayout.addWidget(self.Confirm)
        self.Confirm.clicked.connect(self.confirm_click)
        self.setLayout(mainLayout)


    def confirm_click(self):
        #take out print when done testing

        #Likes
        max_num_likes_input = self.max_number_of_likes.text()
        tags_like_input = self.tags_like.text()
        delay_like_text_input = self.delay_like.text()
        order_like_input = self.order_like.text()
        print("Likes:")
        print(str("Maximum Number of Likes: " + max_num_likes_input))
        print(str("Tags like: " + tags_like_input))
        print(str("Delay for Likes: " + delay_like_text_input))
        #print("\n") #this is for skip
        print(str("Order of Likes: " + order_like_input))
        print("\n")

        #Comments
        print("Comments: ")
        max_num_comments_input = self.max_number_of_comments.text()
        tags_comment_input = self.tags_comment.text()
        delay_comment_input = self.delay_comment.text()
        #skip top 9
        order_like_comment_input = self.order_like_comment.text()
        commment_input_input = self.comment_input.text()
        print(str("Maximum Number of Comments: " + max_num_comments_input))
        print(str("Tags to Comment: " + tags_comment_input))
        print(str("Delay for Comments: " + delay_comment_input))
        #print("\n")  # this is for skip
        print(str("Order of Like Comments: " + order_like_comment_input))
        print(str("Comment Input: " + commment_input_input))
        print("\n")

        #dm
        print("Dms: ")
        max_num_dms_input = self.max_number_of_dms.text()
        dm_input_input = self.dm_input.text()
        #skip top 9
        tags_dm_input = self.tags_dm.text()
        users_dm_input = self.users_dm.text()
        delay_dm_input = self.delay_dm.text()
        print(str("Maximum Number of dms: " + max_num_dms_input))
        print(str("dm input: " + dm_input_input))
        #print("\n")  # this is for skip
        print(str("tags dm: " + tags_dm_input))
        print(str("users dm input: " + users_dm_input))
        print(str("delay dm: " + delay_dm_input))
        print("\n")

        #follow
        print("Follow: ")
        accounts_to_follow_input = self.accounts_to_follow.text()
        follow_followers_input = self.follow_followers.text()
        follow_likers_input = self.follow_likers.text()
        post_index_input = self.post_index.text()
        tags_follow_input =self.tags_follow.text()
        delay_follow_input = self.delay_follow.text()
        #top 9

        print(str("Accounts to follow: " + accounts_to_follow_input))
        print(str("follow_followers " + follow_followers_input))
        print(str("follow likers: " + follow_likers_input))
        print(str("post index: " + post_index_input))
        print(str("tags follow: " + tags_follow_input))
        print(str("delay follow input: " + delay_follow_input))
        #print("\n")  # this is for skip
        print("\n")

        #unfollow
        print("unfollow: ")
        users_unfollow_input =self.users_unfollow.text()
        whitelist_input = self.whitelist.text()
        desired_unfollowing_input =self.desired_unfollowing.text()
        delay_unfollow_input = self.delay_unfollow.text()

        print(str("users to unfollow: " + users_unfollow_input))
        print(str("whitelist " + whitelist_input))
        print(str("desired unfollowing: " + desired_unfollowing_input))
        print(str("delay unfollowing: " + delay_unfollow_input))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())

